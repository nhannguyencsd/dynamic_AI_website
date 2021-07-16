import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from flask import url_for, current_app
import io
import base64
from threading import Thread
import random
import matplotlib.pyplot as plt
import requests

# load weight using thread
def async_load_state_dict(app, model, weight_path, device):
    with app.app_context():
        model.load_state_dict(torch.load(weight_path, map_location=device))
def thread_load_state_dict(model, weight_path, device):
    app = current_app._get_current_object()
    thr = Thread(target=async_load_state_dict, args=[app, model, weight_path, device])
    thr.start()
    return thr

#==================================================================================================================
#                              #HORSE2ZEBRA MODEL                                                                 =
#==================================================================================================================
class HORSE2ZEBRA_ConvolutionalBlock(nn.Module):
    def __init__(self, kernel_name, in_channels, out_channels, kernel_size, stride, padding, activation_name=None):
        super(HORSE2ZEBRA_ConvolutionalBlock, self).__init__()
        kernel_layer = getattr(nn, kernel_name)
        self.covolutional_block = nn.Sequential(
            kernel_layer(in_channels, out_channels, kernel_size, stride, padding, bias=False)
        )
        if activation_name is not None:
            activation = getattr(nn, activation_name) 
            self.covolutional_block.add_module('activation', activation())
                
    def forward(self, x):
        return self.covolutional_block(x)
##--------------------------------------------------------------------------------------------------------------   
class HORSE2ZEBRA_ResidualBlock(nn.Module):
    def __init__(self, in_channels):
        super(HORSE2ZEBRA_ResidualBlock, self).__init__()
        self.residual = nn.Sequential(
            HORSE2ZEBRA_ConvolutionalBlock('Conv2d', in_channels, in_channels, 3, 1, 1, 'ReLU'),
            HORSE2ZEBRA_ConvolutionalBlock('Conv2d', in_channels, in_channels, 3, 1, 1, 'ReLU'))

    def forward(self, x):
        shortcut = x ##shortcut path
        out = self.residual(x) ##main path
        out += shortcut ##gather path
        return out
##--------------------------------------------------------------------------------------------------------------
class HORSE2ZEBRA_MultipleResiduals(nn.Module):
    def __init__(self, in_channels, num_repeat):
        super(HORSE2ZEBRA_MultipleResiduals, self).__init__()
        index = list(range(num_repeat))
        self.multiple_residuals = nn.Sequential()
        for i in range(num_repeat):
            self.multiple_residuals.add_module(f'{index[i]}th_multiple_residuals', HORSE2ZEBRA_ResidualBlock(in_channels))
    
    def forward(self, x):
        return self.multiple_residuals(x)    
##--------------------------------------------------------------------------------------------------------------
class HORSE2ZEBRA_Generator(nn.Module):
    def __init__(self):
        super(HORSE2ZEBRA_Generator, self).__init__()
        ##generator look like autoencoder
        self.generator = nn.Sequential(
            ##encoder part
            ## calculate padding for Conv2d:
                ## (i - k + 2*p)/s + 1 = o round floor
                ## => p = (s(o-1) - i + k)/2 ##round up
                ## if s=1, o=i then p = (1(i-1) - i + k)/2 = (k-1)/2
            ##kernel_name, in_channels, out_channels, kernel_size, stride, padding, activation_name
            HORSE2ZEBRA_ConvolutionalBlock('Conv2d', 3, 64, 7, 1, 3, 'ReLU'), ## i
            HORSE2ZEBRA_ConvolutionalBlock('Conv2d', 64, 128, 3, 2, 1, 'ReLU'), ## i/2
            HORSE2ZEBRA_ConvolutionalBlock('Conv2d', 128, 256, 3, 2, 1, 'ReLU'), ## i/4
            
            ##transformer part
            HORSE2ZEBRA_MultipleResiduals(256, 6), ## i/4
            
            ##decoder part
            ## calculate padding for ConvTranspose2d:
                ##o = s(n-1) + k - 2p
                ##if s=2 then output = 2(n-1) + k - 2p = 2n - 2 + k -2p
            ##kernel_name, in_channels, out_channels, kernel_size, stride, padding, activation_name
            HORSE2ZEBRA_ConvolutionalBlock('ConvTranspose2d', 256, 128, 2, 2, 0, 'ReLU'), ## i/2
            HORSE2ZEBRA_ConvolutionalBlock('ConvTranspose2d', 128, 64, 2, 2, 0, 'ReLU'), ## i
            HORSE2ZEBRA_ConvolutionalBlock('Conv2d', 64, 3, 7, 1, 3, 'Tanh') ## i
        )

    def forward(self, x):
        return self.generator(x) ##output size(set_batch_size, 3, 256, 256)
##--------------------------------------------------------------------------------------------------------------
class HORSE2ZEBRA:
    def get_result(self, input, weight_path):
        #load model
        device = torch.device("cpu")
        G_AB = HORSE2ZEBRA_Generator()
        G_AB.to(device)
        try: 
            thread_load_state_dict(G_AB, weight_path, device)
        except:
            return 'Thread failure'
        ##input image
        input_image = Image.open(input)
        new_image1 = input_image.copy()                            
        ##transfrom image
        custom_transform = transforms.Compose(
            [transforms.Resize((256,256)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])])
        input_image = custom_transform(input_image)
        ##generate new image
        with torch.no_grad():
            real_A = input_image.view(1, 3, 256, 256)
            real_A = real_A.to(device)
            fake_B = G_AB(real_A)
            fake_B = fake_B*0.5 + 0.5
            ###covert batch_out back to an image
            fake_B = fake_B.data.squeeze().cpu()
            new_image2 = transforms.ToPILImage()(fake_B)
        ##img1
        buffered1 = io.BytesIO()
        new_image1.save(buffered1, format='png')
        img_str1 = base64.b64encode(buffered1.getvalue()).decode('utf-8')
        buffered1.truncate(0)
        ##img2
        buffered2 = io.BytesIO()
        new_image2.save(buffered2, format='png')
        img_str2 = base64.b64encode(buffered2.getvalue()).decode('utf-8')
        buffered2.truncate(0)
        ##get result
        result = f'''
        <div class='row mt-5 d-flex'>
            <div class='col-sm-12 col-md-6 text-center mb-2 mt-2'>
                <h3>Input</h3>
                <img class='m-auto w-75 h-75' style='object-fit: cover;' src='data:image/png;base64, {img_str1}'/>
            </div>
            <div class='col-sm-12 col-md-6 text-center mb-2 mt-2'>
                <h3>Output</h3>
                <img class='m-auto w-75 h-75' style='object-fit: cover;' src='data:image/png;base64, {img_str2}'/>
            </div>
        </div>
        <br>
        '''
        del G_AB
        return result


#==================================================================================================================
#                                                   MATH4KID MODEL                                                =
#==================================================================================================================
##HYPER PARMETERS
MATH4KID_latent_dim = 5 ###latent_dim must be the same value like set_latent_dim in training_cgan.ipynb
MATH4KID_number_classes = 10 ###number_classes must be the same value like number_classes in training_cgan.ipynb
## utilizable label function
def MATH4KID_random_onehot_labels(batch_size):
    labels= []
    batch = torch.zeros(batch_size, 10)
    for b in batch:
        label = random.randint(0, 9)
        b[label] = 1
        labels.append(label)
    return labels, batch
##--------------------------------------------------------------------------------------------------------------  
## utilizable model UTILIZABLE MODELS
class MATH4KID_Flatten(nn.Module):
    def forward(self, input):
        return input.view(input.size(0), -1)
##--------------------------------------------------------------------------------------------------------------   
class MATH4KID_Reshape1(nn.Module):
    def forward(self, input):
        return input.view(input.size(0), 256, 4, 4)
##--------------------------------------------------------------------------------------------------------------   
class MATH4KID_Concat(nn.Module):
    def forward(self, x):
        x1 = x[0]
        x2 = x[1]
        return torch.cat((x1, x2), 1)  
##-------------------------------------------------------------------------------------------------------------- 
class MATH4KID_CGAN(torch.nn.Module): ##CGAN: Conditional Generative Adversarial Network
    def __init__(self):
        super(MATH4KID_CGAN, self).__init__()
        ##discrimation part
        self.discriminator_img = nn.Sequential(
            ###batch_sizex1x32x32 => batch_sizex64x16x16
            nn.Conv2d(in_channels=1, out_channels=64, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(0.2)
        )
        self.discriminator_y = nn.Sequential(
            ###batch_sizex10x32x32 => batch_sizex64x16x16
            nn.Conv2d(in_channels=MATH4KID_number_classes, out_channels=64, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(0.2)
            
        )
        self.discriminator = nn.Sequential(
            ###batch_sizex128x16x16
            MATH4KID_Concat(),
            ###batch_sizex128x16x16 => batch_sizex256x8x8
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2),
            ###batch_sizex256x8x8 => batch_sizex512x4x4
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(0.2),
            ###batch_sizex512*4*4
            nn.Flatten(),
            ###batch_sizex1
            nn.Linear(512*4*4, 1, bias=False)
        )

        ##generator part
        self.generator_z = nn.Sequential(
            ###batch_sizex256*4*4
            nn.Linear(MATH4KID_latent_dim, 256*4*4, bias=False),
            nn.BatchNorm1d(256*4*4),
            nn.LeakyReLU(0.2),
            ###batch_sizex256x4x4
            MATH4KID_Reshape1()
        )
        self.generator_y = nn.Sequential(
            ###batch_sizex256*4*4
            nn.Linear(MATH4KID_number_classes, 256*4*4, bias=False),
            nn.BatchNorm1d(256*4*4),
            nn.LeakyReLU(0.2),
            ###batch_sizex256x4x4
            MATH4KID_Reshape1()
        )
        self.generator = nn.Sequential(
            ### batch_sizex512x4x4
            MATH4KID_Concat(), 
            ###batch_sizex512x4x4 => batch_sizex256x8x8
            nn.ConvTranspose2d(in_channels=512, out_channels=256, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2),
            ###batch_sizex256x8x8 => batch_sizex128x16x16
            nn.ConvTranspose2d(in_channels=256, out_channels=128, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2), 
            ###batch_sizex128x16x16 => batch_sizex1x32x32
            nn.ConvTranspose2d(in_channels=128, out_channels=1, kernel_size=4, stride=2, padding=1),
            nn.Tanh()
        )     
    
    def generator_forward(self, z, y):
        out1 = self.generator_z(z)
        out2 = self.generator_y(y)
        return self.generator([out1, out2])
    
    def discriminator_forward(self, img, y):
        out1 = self.discriminator_img(img)
        out2 = self.discriminator_y(y)
        out = self.discriminator([out1, out2])
        return out
##--------------------------------------------------------------------------------------------------------------
class MATH4KID:
    def get_result(self, input, weight_path):
        #load model
        device = torch.device("cpu")
        model = MATH4KID_CGAN()
        model.to(device)
        model.load_state_dict(torch.load(weight_path, map_location=device))
        model.eval()       
        ## make new tensor images
        batch_size = 2
        z = torch.zeros((batch_size, MATH4KID_latent_dim)).uniform_(-1.0, 1.0).to(device)
        actual_labels, y = MATH4KID_random_onehot_labels(batch_size)
        y = y.to(device)
        generated_features = model.generator_forward(z, y)
        imgs = generated_features.view(-1, 32, 32) 
        ##operator
        operator = random.randint(0, 2)
        str_operator = ['+', '-', '*']
        first_operand, second_operand = actual_labels
        if operator == 0: ###addition
            image_operator = Image.open(requests.get('https://raw.githubusercontent.com/nhannguyencsd/vision_math4kid/master/static/inference/plus.jpeg', stream=True).raw)
            answer = first_operand + second_operand
        elif operator == 1: ### subtraction
            image_operator = Image.open(requests.get('https://raw.githubusercontent.com/nhannguyencsd/vision_math4kid/master/static/inference/minus.jpeg', stream=True).raw)
            answer = first_operand - second_operand
        else: ### multiplication
            image_operator = Image.open(requests.get('https://raw.githubusercontent.com/nhannguyencsd/vision_math4kid/master/static/inference/time.jpeg', stream=True).raw)
            answer = first_operand * second_operand 
        ##show operand and operator images
        fig = plt.figure(figsize = (10,2.5))
        ###first operand axis
        ax1 = fig.add_subplot(1,5,1)
        ax1.axis('off')
        ax1.imshow(imgs[0].to(torch.device('cpu')).detach(), cmap='Blues')
        ###second operand axis
        ax2 = fig.add_subplot(1,5,2)
        ax2.axis('off')
        ax2.imshow(image_operator)
        ### third operand axis
        ax3 = fig.add_subplot(1,5,3)
        ax3.axis('off')
        ax3.imshow(imgs[1].to(torch.device('cpu')).detach(), cmap='Blues')
        ### fourth axis
        ax4 = fig.add_subplot(1,5,4)
        ax4.axis('off')
        image_equal = Image.open(requests.get('https://raw.githubusercontent.com/nhannguyencsd/vision_math4kid/master/static/inference/equal.jpeg', stream=True).raw)
        ax4.imshow(image_equal)
        ### fifth axis
        ax5 = fig.add_subplot(1,5,5)
        ax5.axis('off')
        image_question = Image.open(requests.get('https://raw.githubusercontent.com/nhannguyencsd/vision_math4kid/master/static/inference/question.jpeg', stream=True).raw)
        ax5.imshow(image_question)
        plt.show()
        ##buffer
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png')
        img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.truncate(0)
        ## get result
        result = f'''
        <div class='container' style="border: dashed 1px #007bff">
            <div class="row">
                <img class='m-auto w-75 h-75 p-0' src='data:image/png;base64, {img_str}'/>
            </div>
            <div class="row m-0 p-0">
                <p class='m-auto nn-solution-text text-success font-weight-bold' style="display: none; font-size: 20px;">The answer: {first_operand} {str_operator[operator]} {second_operand} = {answer}</p>
            </div>
            <div class="row">
                <button class='btn btn-outline-primary mr-0 mt-0 mb-0 p-1 nn-solution-button' style="border-width: 0">Solution</button>
            </div>
        </div>
        <br><br><br>
        '''
        del model
        return result
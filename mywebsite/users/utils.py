import secrets
import os
from PIL import Image
from mywebsite import  mail
from flask_mail import Message
from flask import url_for, current_app
from threading import Thread

def save_image(form_image):
    #save image part
    hex = secrets.token_hex(8) # use secret instead of bcrypt because bcrypt use for password
    file_name ,file_extension = os.path.splitext(form_image.filename)
    image_filename = hex + file_extension
    image_path = os.path.join(current_app.root_path, 'static/images/user', image_filename)
    #resize image part
    size = (100, 100)
    image = Image.open(form_image) #open the form image not hex image
    image.thumbnail(size)
    image.save(image_path)
    return image_filename

def delete_image(image_filename):
    if image_filename != 'default.png': #make sure it doesn't delete default.png
        image_path = os.path.join(current_app.root_path, 'static/images/user', image_filename)
        if os.path.isfile(image_path): #prevent somehow an image already delete 
            os.remove(image_path)

#first choice of step 2(run slower) of reset password: generate valid token in specific time
#then send a link token to the user who request the reset password 
def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request', sender=current_app.config['MAIL_USERNAME'], recipients=[user.email])
    #note about _external=True: give absolute url
    message.body = f'''Hi {user.username},

Received a request to reset your password. You can reset your password by click the following link. This link is valid for 30 minutes
{ url_for('users.reset_token', token=token, _external=True) } 

If you did not request a password reset, please disregard this email and no changes will be made. 

Kind Reards,
Nhan Nguyen
'''
    mail.send(message)

# second choice step 2(run faster) of reset password: generate valid token in specific time
#then send a link token to the user who request the reset password 
# send reset email faster by using thread
def send_async_reset_email(app, message):
    with app.app_context():
        mail.send(message)
def send_thread_reset_email(user):
    token = user.get_reset_token()
    message = Message('Passwrod Reset Request', sender=current_app.config['MAIL_USERNAME'], recipients=[user.email])
    message.body = f'''Hi {user.username},

Received a request to reset your password. You can reset your password by click the following link. This link is valid for 30 minutes
{ url_for('users.reset_token', token=token, _external=True) } 

If you did not request a password reset, please disregard this email and no changes will be made. 

Kind Reards,
Nhan Nguyen
'''
    app = current_app._get_current_object()
    thr = Thread(target=send_async_reset_email, args=[app, message])
    thr.start()
    return thr
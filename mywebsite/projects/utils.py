from werkzeug.utils import secure_filename
import os
from flask import current_app
from datetime import date

def save_aidotpy(form_file):
    full_file_name = secure_filename(form_file.filename)
    if full_file_name != '': #if full_file_name is not an empty file so it can allow to save the file
        file_name, file_extension = os.path.splitext(form_file.filename)
        if file_name == 'ai': #no need to check .py extension bc it already check in the ProjectForm in the forms.py file
            file_path = os.path.join(current_app.root_path, 'ais', 'ai.py')
            form_file.save(file_path)
            return 'ai.py'
        else:
            return 1
    else:
        return 1   

def save_weight(form_file, model_name):
    full_file_name = secure_filename(form_file.filename)
    if full_file_name != '': #if full_file_name is not an empty name then it can allow to save the file
        file_name, file_extension = os.path.splitext(form_file.filename) #no need to use the filename from the file bc using model_name for filename
        # no need to check file_name bc there are many model weight build on later
        #no need to check [.pt, .pth] extension bc it already check in the ProjectForm in the forms.py file
        full_file_name = model_name + file_extension
        file_path = os.path.join(current_app.root_path, 'static/weights', full_file_name)
        form_file.save(file_path)
        return full_file_name 
    else:
        return 1 

def is_new_day(start, current):
    delta = current - start
    if delta.days >= 1:
        return True
    return False



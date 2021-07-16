from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):
    category = SelectField('Category | Required | Use Choice ', choices=[('',"---"), ('AI',"AI"),('Web',"Web"), ('Electronic', 'Electronic')], validators=[DataRequired()])
    title = StringField('Title | Required | Use Text', validators=[DataRequired()])
    image = StringField('Image | Required | Use Image Adress', validators=[DataRequired()])
    content = TextAreaField('Content | Required | Use Html Tags', validators=[DataRequired()])
    ask_update = SelectField('Model Update | Optional | Use Choice ', choices=[('No',"No"),('Yes',"Yes")], validators=[DataRequired()], default='No')
    model_name = StringField('Model Name | Required | Use Text | WARNING', default='')
    need_input = SelectField('Model Input | Optional | Use Choice ', choices=[('No',"No"),('Yes',"Yes")], default='No') #new
    weight = FileField('Upload Weight | Optional | Use File | WARNING', validators=[FileAllowed(['pt'])])
    aidotpy = FileField('Update ai.py | Optional | Use File | DANGER', validators=[FileAllowed(['py'])])
    submit = SubmitField('Post')
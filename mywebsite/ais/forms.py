from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class AIForm(FlaskForm):
    input = FileField('', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif', 'txt', 'csv'])])
    submit = SubmitField('Run')
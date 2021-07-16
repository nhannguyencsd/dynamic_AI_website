from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class HomeForm(FlaskForm):
    greeting = StringField('My Greeting', validators=[DataRequired()])
    position = StringField('My Position', validators=[DataRequired()])
    about_me_overview = StringField('About Me Overview', validators=[DataRequired()])
    about_me = TextAreaField('About Me', validators=[DataRequired()])
    task = StringField('My Task', validators=[DataRequired()])
    submit = SubmitField('Submit')
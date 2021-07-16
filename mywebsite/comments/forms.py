from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField

class CommentForm(FlaskForm):
    content = TextAreaField('')
    submit = SubmitField('Comment')
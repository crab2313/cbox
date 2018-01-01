from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import *

class UploadComicForm(FlaskForm):
    name = StringField('Comic Name', validators=[DataRequired()])
    archive = FileField('Comic Archive' ,validators=[DataRequired()])
    submit = SubmitField('Upload')
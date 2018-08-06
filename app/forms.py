from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired

class VideoForm(FlaskForm):
    radio = RadioField('Video label', choices=[("5","Straight at intersection"), ("3", "Left at intersection"),
                                               ("4", "Right at intersection"), ("2", "Lane follow"), ("-1", "Not relevant!") ],
                                     validators=[DataRequired()])
    submit = SubmitField('Submit')

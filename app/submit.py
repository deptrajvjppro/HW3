from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class SubmitForm(FlaskForm):
    submitText = StringField('City Name', validators=[DataRequired()])
    submitButton = SubmitField('Submit')

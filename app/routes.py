from app import app_obj
from flask import Flask, render_template, request,session,flash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class SubmitForm(FlaskForm):
    cityname = StringField('City Name', validators=[DataRequired()])
    submitButton = SubmitField('Submit')

@app_obj.route('/', methods = ['GET','POST'])
def home():
    name = 'Lisa'
    city_names = ["Paris","London","Rome","Tahiti"]
    form = SubmitForm()
    if form.validate_on_submit():
        flash(f'{form.cityname.data}')

    return render_template('home.html', name = name, city_names = city_names, form = form)




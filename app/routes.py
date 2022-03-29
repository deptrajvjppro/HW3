from app import app_obj
from flask import Flask, render_template, request,session,abort,flash
from app.submit import LoginForm



@app_obj.route('/',methods = ['GET','POST'])
def hello():
    form = LoginForm()
    name = 'Lisa'
    city_names = ["Paris","London","Rome","Tahiti"]
    if form.validate_on_submit():
        flash(f'{form.cityname.data}')
    return render_template('home.html',title ="Homework3", name = name, city_names=city_names,form = form)


app_obj.run()


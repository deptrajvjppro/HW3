from flask import Flask, render_template, request,session,abort,flash
import os
import jinja2


app_obj = Flask(__name__)
app_obj.config['DEBUG'] =True
name = 'Lisa'
city_names = ["Paris","London","Rome","Tahiti"]

@app_obj.route('/')
def home():
    return f'''<html>
    <head>
        <title>Homework 3</title>
    </head>
    <body>
        <h1>Welcome {name}!</h1>
        <p>
            <a href = "http://www.google.com/" > not google</a>
                <ul>
            <li>{city_names[0]}</li>
            <li>{city_names[1]}</li>
            <li>{city_names[2]}</li>
            <li>{city_names[3]}</li>
        </ul>
        </p>
    </body>
</html>'''

#app_obj.run()



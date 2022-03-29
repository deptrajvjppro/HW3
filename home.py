from flask import Flask, render_template, request,session,abort,flash
import os
import jinja2


app_obj = Flask(__name__)
app_obj.config['DEBUG'] =True

@app_obj.route('/')
def home():
    name = 'Lisa'
    city_names = ["Paris","London","Rome","Tahiti"]
    return f'''<html>
    <head>
        <title>Homework 3</title>
    </head>
    <body>
        <h1>Welcome {name}</h1>
        <p>
            <a href = "https://www.google.com/">not google</a>
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



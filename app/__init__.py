from flask import Flask
from config import Config
import os
SECRET_KEY = os.urandom(32)

app_obj = Flask(__name__)

app_obj.config['SECRET_KEY'] = SECRET_KEY

from app import routes

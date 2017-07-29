from flask import current_app, Flask, redirect, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config) # load config.py
app.secret_key = 'super duper mega secret key'

login_manager = LoginManager() # Login manager for the application
login_manager.init_app(app) # apply login manager
login_manager.login_view = 'home' # set the default redirect page

db = SQLAlchemy(app)
# This imports are necessary for the scope of the directory structure
from app import views
from app import models
from app.views import *

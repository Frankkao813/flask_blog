from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# import from models , from models import 


app = Flask(__name__)
app.config['SECRET_KEY'] = '67a82197c816d8fc3cd2d1658eb8e4d9'
# site.db should be created in the current direcotry
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # similar to url_for() function
login_manager.login_message_category = 'info' # change the style of the text

from flaskblog import routes
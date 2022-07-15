from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# import from models , from models import 


app = Flask(__name__)
app.config['SECRET_KEY'] = '67a82197c816d8fc3cd2d1658eb8e4d9'
# site.db should be created in the current direcotry
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes
# instead of from flaskblog...
# have seen the __main__ module, but haven;t seen db
from flaskblog import db
from datetime import datetime

#create database file
# one to many relationship: a user can have many posts

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # we will going to hash the image
    password = db.Column(db.String(60), nullable=False)
    # lazy=True - Load the data necessary at one time #01(sequence 1)
    posts = db.relationship('Post', backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    data_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    #user.id -> tablename.columnname (lowercase)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.title}', '{self.data_posted}')"

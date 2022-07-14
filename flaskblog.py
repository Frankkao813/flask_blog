from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = '67a82197c816d8fc3cd2d1658eb8e4d9'
# site.db should be created in the current direcotry
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

#create database file
# one to many relationship: a user can have many posts
db = SQLAlchemy(app)
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


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
     {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

# about page: talk about why the website is established, and offer some tips
# to use the website
@app.route("/about")
def about():
    return render_template('about.html', title = "about")

# list the allowed method here -http method
# when the password different - will return an error
@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # validate when submit
        flash(f'Account created for {form.username.data}!', 'success')
        # redirect the user to the home page
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form  = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'trial@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            # redirect to the home page
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessgful. Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


# make a custom 404, 500 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
	app.run(debug=True) 
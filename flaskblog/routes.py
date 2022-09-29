# this file contains all the route of the website
from flask import render_template, url_for, flash, redirect
# import from __init__.py
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    # make sure that after login/register, the user won't return to the login/register page after clicking the button
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # from forms.py. The .validate_on_submit method will be executed to check
    # if check fails, register.html will run the error message set from register.html and forms.py
    form = RegistrationForm()
    if form.validate_on_submit(): 
        # add new user into the database
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in!', 'success')
        # redirect the user to the home page
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form  = LoginForm()
    if form.validate_on_submit():
        #if form.email.data == 'trial@blog.com' and form.password.data == 'password':
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    # simply return the login page
    return render_template('login.html', title='Login', form=form)


# make a custom 404, 500 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

# logout route for flaskblog
# we also have to alter the jinja2 template at layout.html
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required # need to login to access this route
def account():
    return render_template('account.html', title='Account')
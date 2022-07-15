from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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

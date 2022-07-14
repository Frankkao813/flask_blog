from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# secret key - protect the site from malicious attacks
# how to generate random string? -> import secrets, secrets.token_hex(16)
app.config['SECRET_KEY'] = '67a82197c816d8fc3cd2d1658eb8e4d9'

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
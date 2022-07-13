from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello_world():
    return render_template('home.html', posts=posts)

# about page: talk about why the website is established, and offer some tips
# to use the website
@app.route("/about")
def about():
    return render_template('about.html', title = "about")

# make a custom 404, 500 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
	app.run(debug=True) 
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
    'author' : 'Valentin Cantu',
    'title' : 'First blog post',
    'content' : 'Im making a website',
    'date_posted' : 'October 26, 2018'
    },
    {
    'author' : 'Valentin Cantu',
    'title' : 'Second blog post',
    'content' : 'This is dummy data',
    'date_posted' : 'October 26, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About SneakerHub')



if __name__ == '__main__':
    app.run(debug=True)
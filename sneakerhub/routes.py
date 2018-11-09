from flask import render_template, url_for, flash, redirect
from sneakerhub import app
from sneakerhub.forms import RegistrationForm, LoginForm
from sneakerhub.models import User, Post

posts = [
    {
        'author': 'Valentin Cantu',
        'title': 'First blog post',
        'content': 'Im making a website',
        'date_posted': 'October 26, 2018'
    },
    {
        'author': 'Valentin Cantu',
        'title': 'Second blog post',
        'content': 'This is dummy data',
        'date_posted': 'October 26, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About SneakerHub')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register SneakerHub Account', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed', 'danger')
    return render_template('login.html', title='Login to SneakerHub', form=form)

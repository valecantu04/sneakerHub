from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '28de2b94c37cfc019aea54bd566e012f'

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


@app.route("/register", methods=['GET','POST'])
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


if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Calle'}
    posts = [
        {
            'author': {'username': 'Olle'},
            'body': 'Snart jul!'
        },
        {
            'author': {'username': 'Sussie'},
            'body': 'Kalle Anka!'
        }
    ]
    return render_template('index.html', title='Homepage', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

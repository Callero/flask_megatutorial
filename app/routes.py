from flask import render_template
from app import app

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

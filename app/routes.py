from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Calle'}
    return render_template('index.html', title='Homepage', user=user)

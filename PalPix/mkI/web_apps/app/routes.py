from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Brendan'}
    posts = [
        {
            'author': {'username': 'Maise'},
            'body': 'Homeward Bound!'
        },
        {
            'author': {'username': 'Derek'},
            'body': 'Zoolander'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
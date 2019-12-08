from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'rayhan'}
    posts = [
        {
            'author': {'username': 'rayhan'},
            'body': 'Beautiful day in Victoria!'
        },
        {
            'author': {'username': 'John'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

from flask import  render_template
from app import app
user = {'name':'Trump'}
@app.route('/')
def index():
    user = {'name': 'Trump'}
    posts = [
        {
            'author':{'name':'George'},
            'body':'WOW!'
        },
        {
            'author':{'name':'Wallace'},
            'body':'Amazing!'
        }
    ]
    return render_template("index.html",user = user,posts=posts)
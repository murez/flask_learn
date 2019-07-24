from flask import  render_template
from app import app
user = {'name':'Trump'}
@app.route('/')
@app.route('/index')
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
    return render_template("index.html",title='O',user = user,posts=posts)
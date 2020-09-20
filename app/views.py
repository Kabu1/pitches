from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its date
    '''
    title = 'Home - Welcome to the Pitch Website'
    return render_template('index.html',title=title)
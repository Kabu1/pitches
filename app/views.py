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
@app.route('/categories')

def index():

    '''
    View root page function that returns the index page and its data
    '''
    general = Pitch.query.filter_by(category="general").order_by(Pitch.posted.desc()).all()
    project = Pitch.query.filter_by(category="project").order_by(Pitch.posted.desc()).all()
    advertisement = Pitch.query.filter_by(category="advertisement").order_by(Pitch.posted.desc()).all()
    sale = Pitch.query.filter_by(category="sale").order_by(Pitch.posted.desc()).all()

    pitch = Pitch.query.filter_by().first()
    likes = Like.get_all_likes(pitch_id=Pitch.id)
    dislikes = Dislike.get_all_dislikes(pitch_id=Pitch.id)


    title = 'Home | One Min Pitch'
    return render_template('index.html', title = title, pitch = pitch, general = general, project = project, advertisement = advertisement, sale = sale, likes=likes, dislikes=dislikes)

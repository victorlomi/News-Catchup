from flask import render_template, flash, redirect, url_for
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    news_source = {
        'name': 'vox news',
        'description': 'The best news source for the woke millenial.',
        'image': 'images/vox.jpg',
    }
    return render_template('index.html', news_source=news_source) 

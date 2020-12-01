from flask import render_template, flash, redirect, url_for, request
from app.source import bp

def separate_names(name, character='-'):
    """Split the names and return them as one string"""
    names = name.split(character) 
    final_name = ''
    for s in names:
        final_name += f'{s} '
    return final_name.strip() 

@bp.route('/source')
def search_source():
    source = request.args.get('q') 
    return render_template('source.html', source=source, separate_names=separate_names) 


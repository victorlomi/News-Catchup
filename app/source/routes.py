from flask import render_template, flash, redirect, url_for, request
from app.source import bp

@bp.route('/source')
def search_source():
    source = request.args.get('q') 
    return f'your source is {source}'


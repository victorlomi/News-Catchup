import datetime
import os
from flask import render_template, flash, redirect, url_for, request
import requests
from app.source import bp

def simplify_date(date):
    return date[0:10]

@bp.route('/source')
def search_source():
    API_KEY = os.environ.get('API_KEY')
    news_source = request.args.get('q')

    url = f"https://newsapi.org/v2/top-headlines?sources={news_source}&apiKey={API_KEY}"
    response = requests.get(url).json()
    
    return render_template('source.html', source=news_source, articles=response["articles"], simplify_date=simplify_date, api_key=API_KEY) 


import datetime
import os
from flask import render_template, flash, redirect, url_for, request
import requests
from app.source import bp

from app.models import article as at

def simplify_date(date):
    return date[0:10]

@bp.route('/source')
def search_source():
    API_KEY = os.environ.get('API_KEY')
    news_source = request.args.get('q')

    url = f"https://newsapi.org/v2/top-headlines?sources={news_source}&apiKey={API_KEY}"
    response = requests.get(url).json()

    # create article objects 
    articles = []
    for article in response["articles"]:
        articles.append(at.Article(
            article["source"], article["author"], article["title"], article["description"],
            article["url"], article["urlToImage"], article["publishedAt"], article["content"]))
    
    return render_template('source.html', source=news_source, articles=articles, simplify_date=simplify_date, api_key=API_KEY) 


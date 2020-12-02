import os
from flask import render_template, flash, redirect, url_for, request
import requests
from app.source import bp

from app.models import article as at

def simplify_date(date):
    """Simplify the date so that it only contains year-month-day."""
    return date[0:10]

@bp.route('/source')
def search_source():
    """Show this view when a source is pressed and show articles."""
    API_KEY = os.environ.get('API_KEY')
    news_source = request.args.get('q')

    # Make the request and change the response to a dict we can use.
    url = f"https://newsapi.org/v2/top-headlines?sources={news_source}&apiKey={API_KEY}"
    response = requests.get(url).json()

    # create article objects and store them in a list.
    articles = []
    for article in response["articles"]:
        articles.append(at.Article(
            article["source"], article["author"], article["title"], article["description"],
            article["url"], article["urlToImage"], article["publishedAt"], article["content"]))
    
    return render_template('source.html', source=news_source, articles=articles, simplify_date=simplify_date, api_key=API_KEY) 


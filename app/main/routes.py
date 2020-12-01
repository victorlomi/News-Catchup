from flask import render_template, flash, redirect, url_for
from app.main import bp
from app.main import source

@bp.route('/')
def index():
    images = {
        'bbc': 'images/bbc.png',
        'bbcsports': 'images/bbcsports.jpg',
        'billboard': 'images/billboard.jpg',
        'bleacher_report': 'images/bleacher-report.jpg',
        'bloomberg': 'images/bloomberg.png',
        'business_insider': 'images/business-insider.png',
        'buzzfeed': 'images/buzzfeed.png',
        'cbc-news': 'images/cbc-news.jpg',
        'cnn': 'images/cnn.jpg',
        'espn': 'images/espn.png',
        'fox': 'images/fox.jpg',
        'polygon': 'images/polygon.png',
    }

    news_sources = {
        'bbc': source.Source('bbc-news', 'BBC News', images['bbc']), 
        'bbc_sports': source.Source('bbc-sport', 'BBC Sport', images['bbcsports']), 
        'billboard': source.Source("billboard", "Billboard", images['billboard']), 
        'bleacher_report': source.Source("bleacher-report", "Bleacher Report", images['bleacher_report']), 
        'bloomberg': source.Source("bloomberg", "Bloomberg", images['bloomberg']), 
        'business_insider': source.Source("business-insider", "Business Insider", images['business_insider']), 
        'buzzfeed': source.Source("buzzfeed", "Buzzfeed", images['buzzfeed']), 
        'cbc_news': source.Source("cbc-news", "CBC News", images['cbc-news']), 
        'cnn': source.Source("cnn", "CNN", images['cnn']), 
        'espn': source.Source("espn", "ESPN", images['espn']), 
        'fox': source.Source("fox-news", "Fox News", images['fox']), 
        'polygon': source.Source("polygon", "Polygon", images['polygon']), 
    }
    return render_template('index.html', news_sources=news_sources) 

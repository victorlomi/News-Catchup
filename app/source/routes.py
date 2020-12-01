import datetime
from flask import render_template, flash, redirect, url_for, request
from app.source import bp

def simplify_date(date):
    return date[0:10]

@bp.route('/source')
def search_source():
    article = {
        "title": "Analysis: The fate of millions of Americans rests on Biden's economic team",
        "description": "Joe Biden's incoming economic team will shoulder the desperate hopes of millions of Americans who have lost jobs, face eviction from their homes or who are going hungry in a monstrous Covid-19-induced slump.",
        "url": "http://us.cnn.com/2020/12/01/politics/joe-biden-economic-team-white-house/index.html",
        "urlToImage": "https://cdn.cnn.com/cnnnext/dam/assets/201123153507-janet-yellen-super-tease.jpg",
        "publishedAt": "2020-12-01T05:01:13Z",
    }
    source = request.args.get('q') 
    return render_template('source.html', source=source, article=article, simplify_date=simplify_date) 


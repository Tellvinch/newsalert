from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_updates, get_articles



# Views


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    political_news = get_updates('politics')
    business_news = get_updates('business')
    technology_news = get_updates('technology')
    entertainment_news = get_updates('entertainment')
    title = 'NewsAlert'
    return render_template('index.html', title=title,politics=political_news, business=business_news, technology=technology_news, entertainment=entertainment_news)


@main.route('/templates/update/<id>')
def source(id):
    articles = get_articles(id)
    print(articles)
    return render_template('update.html', articles=articles)

from flask import render_template
from app import app
from .request import get_newss,get_news


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    general_news = get_newss('general')    
    science_news = get_newss('science')
    entertainment_news = get_newss('entertainment')
    health_news = get_newss('health')
    sports_news = get_newss('sports')
    technology_news = get_newss('technology')
    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title,science = science_news,technology = technology_news,sports = sports_news,health = health_news,general = general_news,entertainment = entertainment_news)


@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    title = f'You are viewing {news_id}'
    return render_template('news.html',title = title,news = news)
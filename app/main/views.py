from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_movies, get_movie, search_movie
from ..models import Review


# Views
@main.route('/')
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
    return render_template('index.html', title=title, science=science_news, technology=technology_news, sports=sports_news, health=health_news, general=general_news, entertainment=entertainment_news)


@main.route('/news/<int:id>')
def news(id):
    '''
    View news page function that returns the movie details page and its data
    '''
    movie = get_news(id)
    title = "Werokam"

    return render_template('news.html', title=title, news=news)

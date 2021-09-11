from app.request import get_news
from flask import render_template
from app import app
from .request import get_news1,get_news2

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    trending_news = get_news('trending')
    current_news = get_news('current')
    world_wide_news = get_news('World')
    title = 'Home - Welcome to The best News Website Online'
    head = 'todays headlines'
    return render_template('index.html',title = title,head = head,trending = trending_news,current = current_news,world = world_wide_news)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news2(id)
    title = f'{news.title}'
    return render_template('news.html',id = news_id,news = news,title = title)

from flask import render_template
from app import app
from flask import render_template,request,redirect,url_for
from .request import get_news1,get_news2,search_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    trending_news = get_news1('trending')
    current_news = get_news1('current')
    world_wide_news = get_news1('World')
    title = 'Home - Welcome to The best News Website Online'
    head = 'todays headlines'

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html',title = title,head = head,trending = trending_news,current = current_news,world = world_wide_news)
    

@app.route('/news/<news_id>')
def news(news_id):
    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news2(id)
    title = f'{news.title}'
    return render_template('news.html',id = news_id,news = news,title = title)

@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)

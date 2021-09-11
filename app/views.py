from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best News Website Online'
    head = 'toadys headlines'
    return render_template('index.html',title = title,head = head)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)

from flask import Flask, render_template, redirect, request, url_for, session
from pymongo import MongoClient
from bson.objectid import ObjectId
import os



app = Flask(__name__)
app.secret_key = 'some secret'

cluster = MongoClient("mongodb+srv://admin:JVRSz9vj3ROJUNqF@articlescluster.e9swl.mongodb.net/article-manager?retryWrites=true&w=majority")


db = cluster['article-manager']
articles = db['articles']
users = db['users']

@app.route('/')



@app.route('/index')
def index():
    return render_template('index.html',
                            articles=db['articles'])

@app.route('/all_articles')
def all_articles():
    return render_template("allarticles.html",
                            articles=db['articles'])

@app.route('/get_article/<article_id>')
def get_article(article_id):
    articles = db['articles']
    the_article = articles.find_one({"_id": ObjectId(article_id)})
    return render_template("getarticle.html",
                            article=the_article)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if 'username' in session:
        return render_template('index.html',
                                message='You are already signed in!')
    if request.method == 'POST':
        users = db['users']
        user_signin = users.find_one({'username': request.form['username']})
        if user_signin:
            if request.form['password'] == user_signin['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        return render_template('signin.html',
                                    message='Invalid username or password')
    return render_template('signin.html', message='')

@app.route('/signout')
def signout():
    if 'username' in session:
        session.pop('username')
        return render_template('message.html',
                                message='Signed out. See you later!')
    return render_template('message.html',
                            message='You have already signed out!')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return render_template('register.html',
                                message='You are already signed in and registered')
    if request.method== 'POST':
        users = db['users']
        existing_user = users.find_one({'username': request.form['username']})
        if request.form['username'] and request.form['password']:
            if existing_user is None:
                password = request.form['password']
                users.insert_one({'username': request.form['username'],
                                'password': password})
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            return render_template('register.html', message='Username ' + str(existing_user['username']) + ' already exists')
        return render_template('register.html', message='Enter a username and password')
    return render_template('register.html', message='')

@app.route('/<username>/add_article', methods=['GET', 'POST'])
def add_article(username):
    if 'username' in session:
        username = session['username']
        if request.method == 'POST':
            article = db['articles']
            article.insert_one({
                'article_name': request.form['article_name'],
                'article_content': request.form['article_content'],
                'article_author': session['username'],
            })
        return render_template('addarticle.html',
                                username=session['username'])
    return render_template('signin.html')

@app.route('/my_articles/<username>')
def my_articles(username):
    if 'username' in session:
        user = db['users'].find_one({'username':username})
        user_articles = db['articles'].find({"article_author": session['username']})
        return render_template('myarticles.html',
                                user=user,
                                user_articles=user_articles,
                                message='Your articles')
    else:
        return redirect(url_for('index',
                                message='You have not submitted any articles!'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', 5000)),
    debug=True)


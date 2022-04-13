import os
from flask import Flask, render_template, redirect, request, url_for, session  
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import math

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'article-manager'
app.config["MONGO_URI"] = 'mongodb+srv://admin:pWSlyvkLUOph5go0@articlescluster.e9swl.mongodb.net/article-manager'
mongo = PyMongo(app)

@app.route('/')

@app.route('/index')
def index():
    return render_template ("index.html",
    article=mongo.db.articles.find({"article_name"}))

@app.route('/getarticle')
def get_article(article_id):
    the_article = mongo.db.articles.find_one({"_id": ObjectId(article_id)})
    article_name = the_article['article_name']
    return render_template ("getarticle.html",
    article=the_article,
    article_name=article_name)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', 5000)),
    debug=True)


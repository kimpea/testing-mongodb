from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import math
import os


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'article-manager'
app.config["MONGO_URI"] = 'mongodb+srv://admin:pWSlyvkLUOph5go0@articlescluster.e9swl.mongodb.net/article-manager'
mongo = PyMongo(app)
db = mongo.db

@app.route('/')

@app.route('/index')
def index():
    return render_template("index.html",
                            articles=db.articles.find())


@app.route('/get_article/<article_id>')
def get_article(article_id):
    the_article = db.articles.find_one({"_id": ObjectId(article_id)})
    return render_template("getarticle.html",
                            article=the_article)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', 5000)),
    debug=True)


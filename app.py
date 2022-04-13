import os
from flask import Flask, render_template, redirect, request, url_for, session  
from flask_pymongo import PyMongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import math

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'article-manager'
app.config["MONGO_URI"] = "mongodb+srv://kimpearton:<ehCCRM3DC6yY8Du>@cluster0.xuetz.mongodb.net/article-manager?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')

@app.route('/index')
def index():
    return render_template ("index.html")


@app.route('/getarticle', methods=['GET'])
def get_article(article_id):
    the_article = mongo.db.articles.find({"_id": ObjectId(article_id)})
    return render_template("getarticle.html",
                            article=the_article)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)


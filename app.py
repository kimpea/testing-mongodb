import os
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import math

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'article-manager'
app.config["MONGO_URI"] = 'mongodb+srv://admin:pWSlyvkLUOph5go0@articlescluster.e9swl.mongodb.net/article-manager'
mongo = PyMongo(app)
db = mongo.db

@app.route('/')

@app.route('/index', methods=['GET'])
def index():
    articles = db.articles.find()
    articles = list(articles)
    return render_template("index.html",
                            articles=articles)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', 5000)),
    debug=True)


from flask import Flask, render_template, url_for
from flask_pymongo import pymongo
from bson.objectid import ObjectId
import os


app = Flask(__name__)

CONNECTION_STRING = 'mongodb+srv://admin:pWSlyvkLUOph5go0@articlescluster.e9swl.mongodb.net/article-manager'
client = pymongo.MongoClient('CONNECTION_STRING')
db = client.get_database('article-manager')
articles_collection = pymongo.collection.Collection(db, 'articles')

@app.route('/test')
def test():
    db.db.collection.insert_one({"article_name": "Test Article"})
    return "Connected to the data base!"



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', 5000)),
    debug=True)


import os
from flask import Flask, render_template, redirect, request, url_for, session  
from flask_pymongo import PyMongo
"""
from bson.objectid import ObjectId
"""
import math

app = Flask(__name__)

mongo = PyMongo(app)
client = mongo.MongoClient("mongodb+srv://kimpearton:<ehCCRM3DC6yY8Du>@cluster0.xuetz.mongodb.net/article-manager?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test


@app.route('/')



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)


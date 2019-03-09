import os
import urllib.parse
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_pymongo import PyMongo


from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

user = urllib.parse.quote_plus(os.getenv("MONGO_USERNAME"))
pw = urllib.parse.quote_plus(os.getenv("MONGO_PASSWORD"))
app.config["MONGO_URI"] = f"mongodb://{ user }:{ pw }@mongo:27017/posts?authSource=admin"
mongo = PyMongo(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello')


class User(Resource):
    def get(self):
        mongo.db.posts.insert_one({"name":"hello_daisy"})
        return jsonify("Hello Char")


api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

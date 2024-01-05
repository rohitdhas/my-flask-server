# Tutorial Link - https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24

from flask import Flask, jsonify, request
from settings import MONGODB_URI
from pymongo import MongoClient
from bson import json_util
from bson import ObjectId
import certifi
import json

app = Flask(__name__)
client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())

main_db = client.main
user_collection = main_db.get_collection("user")


def parse_json(data):
    return json.loads(json_util.dumps(data))


@app.route("/", methods=["GET"])
def main():
    return jsonify({"message": "Hello from Flask!"})


@app.route("/user/get_all", methods=["GET"])
def get_all_users():
    users = user_collection.find()
    return jsonify({"users": parse_json(users)})


@app.route("/user/<string:user_id>", methods=["GET", "PATCH", "DELETE"])
def get_user(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)})

    if user is None:
        return jsonify({"error": "User not found!"}), 404

    return jsonify({"user": parse_json(user)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

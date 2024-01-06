from settings import MONGODB_URI
from pymongo import MongoClient
from bson import ObjectId
from utils import parse_json
import certifi

client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())

main_db = client.main
user_collection = main_db.get_collection("user")


def get_all_users():
    users = user_collection.find()
    return {"users": parse_json(users)}, 200


def get_user_by_id(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)})

    if user is None:
        return {"error": "User not found!"}, 404

    return {"user": parse_json(user)}, 200


def create_user(user_details):
    if not user_details:
        return {"error": "No data provided!"}, 400

    user_collection.insert_one(user_details)
    return {"message": "Successfully created user!"}, 200


def update_user(user_id, user_details):
    if not user_details:
        return {"error": "No data provided!"}, 400

    user = user_collection.find_one({"_id": ObjectId(user_id)})

    if user is None:
        return {"error": "User not found!"}, 404

    user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_details})

    return {"message": "Successfully updated user details!"}, 200


def delete_user(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)})

    if user is None:
        return {"error": "User not found!"}, 404

    user_collection.delete_one({"_id": ObjectId(user_id)})
    return {"message": "User deleted!"}, 200

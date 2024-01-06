# Tutorial Link - https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24

from flask import Flask, jsonify, request
from user import get_user_by_id, get_all_users, update_user, delete_user, create_user

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return jsonify({"message": "Hello from Flask!"}), 200


@app.route("/user/get_all", methods=["GET"])
def get_all():
    all_users = get_all_users()
    return jsonify(all_users), 200


@app.route("/user/", methods=["POST"])
def create_new_user():
    user_data = request.json
    result, status_code = create_user(user_data)
    return jsonify(result), status_code


@app.route("/user/<string:user_id>", methods=["GET", "PATCH", "DELETE"])
def handle_user(user_id):
    match request.method:
        case "GET":
            user, status_code = get_user_by_id(user_id)
            return jsonify(user), status_code
        case "PATCH":
            result, status_code = update_user(user_id, request.json)
            return jsonify(result), status_code
        case "DELETE":
            result, status_code = delete_user(user_id)
            return jsonify(result), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

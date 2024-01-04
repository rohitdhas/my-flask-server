# Tutorial Link - https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24

from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "rohit"},
    {"id": 2, "name": "vaibhav"},
    {"id": 3, "name": "vikas"},
    {"id": 4, "name": "sankalp"},
]


@app.route("/", methods=["GET", "POST"])
def main():
    return jsonify({"message": "Hello from Flask!"})


@app.route("/user/<int:user_id>/")
def hello(user_id):
    found_user = None
    for user in users:
        if user["id"] == user_id:
            found_user = user
            break

    if found_user != None:
        return jsonify(user), 200
    return {"error": "User not found!"}, 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

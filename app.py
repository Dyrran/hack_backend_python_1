from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/users", methods=["GET"])
def users():
    return jsonify({
        "payload": "success"
    })

@app.route("/user", methods=["DELETE"])
def user():
    return jsonify({
        "payload": "success"
    })


if __name__ == "__main__":
    app.run(debug=True)
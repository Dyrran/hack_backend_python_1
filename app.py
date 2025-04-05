from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# H-1
@app.route("/users", methods=["GET"])
def users():
    return jsonify({
        "payload": "success"
    })

# H-2
@app.route("/user", methods=["POST"])
def useradd():
    return jsonify({
        "payload": "success"
    })

# H-3
@app.route("/user", methods=["DELETE"])
def userdel():
    return jsonify({
        "payload": "success"
    })

# H-4 ERROR
@app.route("/user", methods=["PUT"])
def useredit():
    return jsonify({
        "payload": "success"
    })

# H-5
@app.route("/api/v1/users", methods=["GET"])
def userget():
    return jsonify({
        "payload": []
    })

# H-6 FAILED
@app.route("/api/v1/user", methods=["POST"])
def user_addargs():
    email = request.args.get('email')
    name = request.args.get('name')
    
    return jsonify({
        "payload": {
            "email": email,
            "name": name
        }
    })

# H-7
@app.route("/api/v1/user/add", methods=["POST"])
def user_register_form():
    email = request.form.get("email")
    name = request.form.get("name")
    id = request.form.get("id")

    return jsonify({
        "payload": {
            "email": email,
            "name": name,
            "id": id
        }
    })

# H-8
@app.route("/api/v1/user/create", methods=["POST"])
def user_register_json():
    data = request.get_json()

    return jsonify({
        "payload": {
            "email": data["email"],
            "name": data["name"],
            "id": data["id"]
        }
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
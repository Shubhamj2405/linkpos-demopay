from flask import Blueprint, request, jsonify
import uuid
import bcrypt
from services.dynamodb_service import users_table
from services.jwt_service import generate_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    user_id = str(uuid.uuid4())

    hashed_password = bcrypt.hashpw(
        data["password"].encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    users_table.put_item(
        Item={
            "userId": user_id,
            "name": data["name"],
            "email": data["email"],
            "password": hashed_password
        }
    )

    return jsonify({"message": "User registered successfully"})


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    response = users_table.scan()
    users = response.get("Items", [])

    for user in users:
        if user["email"] == data["email"]:
            valid = bcrypt.checkpw(
                data["password"].encode("utf-8"),
                user["password"].encode("utf-8")
            )

            if valid:
                token = generate_token(user["userId"])

                return jsonify({
                    "token": token,
                    "userId": user["userId"],
                    "name": user["name"]
                })

    return jsonify({"message": "Invalid credentials"}), 401
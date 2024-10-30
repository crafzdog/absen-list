from flask import Blueprint, request, jsonify

from src.models import db
from src.models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"username": new_user.username, "password": new_user.password}), 200

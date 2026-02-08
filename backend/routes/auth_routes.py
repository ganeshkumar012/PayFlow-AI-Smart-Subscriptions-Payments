from flask import Blueprint, jsonify
from models.user import User
from app import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([
        {"id": u.id, "email": u.email, "role": u.role}
        for u in users
    ])

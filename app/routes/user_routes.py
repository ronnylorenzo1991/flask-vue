from flask import Blueprint

from app.controllers.user_controller import delete, create, update, all

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/api/users/<int:id>", methods=["DELETE"])(delete)
user_bp.route("/api/users", methods=["POST"])(create)
user_bp.route("/api/users/<int:id>", methods=["PUT"])(update)
user_bp.route("/api/users", methods=['GET'])(all)

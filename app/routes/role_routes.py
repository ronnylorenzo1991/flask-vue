from flask import Blueprint

from app.controllers.role_controller import delete, create, update, all, toggle_permission

role_bp = Blueprint("role_bp", __name__)

role_bp.route("/api/roles/<int:id>", methods=["DELETE"])(delete)
role_bp.route("/api/roles", methods=["POST"])(create)
role_bp.route("/api/roles/<int:id>", methods=["PUT"])(update)
role_bp.route("/api/roles", methods=['GET'])(all)
role_bp.route("/api/roles/toggle_permission/<int:id>", methods=['POST'])(toggle_permission)

from flask import Blueprint

from app.controllers.permission_controller import delete, create, update, all

permission_bp = Blueprint("permission_bp", __name__)

permission_bp.route("/api/permissions/<int:id>", methods=["DELETE"])(delete)
permission_bp.route("/api/permissions", methods=["POST"])(create)
permission_bp.route("/api/permissions/<int:id>", methods=["PUT"])(update)
permission_bp.route("/api/permissions", methods=['GET'])(all)

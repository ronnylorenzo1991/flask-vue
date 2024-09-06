from flask import Blueprint, render_template, jsonify, request
from flask_login import current_user, login_user
from app.forms.user_form import LoginForm
from app.models.user_model import User
from flask_jwt_extended import create_access_token
from app import bcrypt, jwt, db
from app.controllers.auth_controller import login, is_authenticated
from app.controllers.default_controller import get_lists

bp = Blueprint("main", __name__)


@bp.route("/", defaults={"path": ""})
@bp.route("/<path:path>")
def render_vue(path):
    return render_template("index.html")


bp.route("/api/login", methods=["POST"])(login)
bp.route("/api/is_authenticated", methods=["GET"])(is_authenticated)
bp.route("/api/lists", methods=["GET"])(get_lists)

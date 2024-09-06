from flask import jsonify
from flask_login import current_user, login_user
from app.forms.user_form import LoginForm
from app.models.user_model import User
from flask_jwt_extended import create_access_token
from app import bcrypt


def is_authenticated():
    if current_user.is_authenticated:
        access_token = create_access_token(identity={"username": current_user.username})
        return (
                jsonify(
                    {
                        "message": "El usuario ya se encuentra autenticado",
                        "token": access_token,
                        "user": {"email": current_user.email, "username": current_user.username},
                        "permissions": current_user.get_permissions(),
                        "roles": current_user.get_roles(),
                    }
                ),
                200,
            )

    return jsonify({"success": "Proceda a iniciar sesion"})
    
def login():
    if current_user.is_authenticated:
        access_token = create_access_token(identity={"username": user.username})
        return (
                jsonify(
                    {
                        "message": "El usuario ha iniciado sesión",
                        "token": access_token,
                        "user": {"email": current_user.email, "username": current_user.username},
                        "permissions": current_user.get_permissions(),
                        "roles": current_user.get_roles(),
                    }
                ),
                200,
            )

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            access_token = create_access_token(identity={"username": user.username})
            return (
                jsonify(
                    {
                        "token": access_token,
                        "user": {"email": user.email, "username": user.username},
                        "permissions": user.get_permissions(),
                        "roles": user.get_roles(),
                    }
                ),
                200,
            )
        else:
            return (
                jsonify(
                    {
                        "errors": [
                            "No existen registros con esa combinación de usuario y clave"
                        ]
                    }
                ),
                401,
            )
    else:
        return jsonify({"errors": form.errors})

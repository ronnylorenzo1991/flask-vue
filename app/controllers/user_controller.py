from app.models.user_model import User
from app.models.user_role_model import UserRole
from app.models.role_model import Role
from app import db, bcrypt
from app.forms.user_form import UserForm
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy import asc, desc
from ast import literal_eval


@jwt_required()
def all():
    current_page = request.args.get("page", 1, type=int)
    per_page = request.args.get("perPage", 10, type=int)

    # Filters
    search_name = request.args.get("username", "", type=str)
    search_email = request.args.get("email", "", type=str)
    search_role = request.args.get("role", "", type=int)
    sort_by = request.args.get("sortBy", "id", type=str)
    sort_order = request.args.get("sortDir", "desc", type=str)

    query = User.query
    if search_name:
        query = query.filter(User.username.like(f"%{search_name}%"))
    if search_email:
        query = query.filter(User.email.like(f"%{search_email}%"))
    if search_role:
        query = query.join(UserRole).join(Role).filter(Role.id == search_role)

    if sort_by in ["username", "email", "id"]:
        if sort_order == "desc":
            query = query.order_by(desc(getattr(User, sort_by)))
        else:
            query = query.order_by(asc(getattr(User, sort_by)))

    pagination = query.paginate(page=current_page, per_page=per_page)
    data = get_pagination(pagination, current_page, per_page)
    return jsonify(data)


@jwt_required()
def create():
    form = UserForm()
    roles = form.roles.data
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash("secret").decode("utf-8")
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )

        for role in roles:
            user.roles.append(Role.query.filter_by(id=role).first())

        db.session.add(user)
        db.session.commit()

        return (
            jsonify(
                {"message": "User created successfully", "user": user_to_dict(user)}
            ),
            200,
        )
    else:
        return jsonify({"errors": form.errors}), 422


@jwt_required()
def update(id):
    user = User.query.get_or_404(id)
    form = UserForm(obj=user)

    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.roles = [Role.query.get(role_id) for role_id in form.roles.data]

        db.session.commit()

        return (
            jsonify(
                {"message": "User updated successfully", "user": user_to_dict(user)}
            ),
            200,
        )
    else:
        return jsonify({"errors": form.errors}), 422


@jwt_required()
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return (
        jsonify({"message": "User removed successfully"}),
        200,
    )


def get_pagination(pagination, current_page, per_page):
    base_url = request.base_url
    links = []

    for page in range(pagination.pages):
        link = {
            "label": str(page + 1),
            "url": f"{base_url}?page={page + 1}",
            "active": page + 1 == current_page,
        }
        links.append(link)

    offset = (current_page - 1) * per_page + 1
    to = ((current_page - 1) * per_page + 1) + per_page - 1
    if to > pagination.total:
        to = pagination.total

    return {
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page,
        "links": links,
        "users": [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "roles": [rol.id for rol in user.roles],
            }
            for user in pagination.items
        ],
        "from": offset,
        "to": to,
        "prev_page": (
            f"{base_url}?page={pagination.prev_num}" if pagination.has_prev else None
        ),
        "next_page": (
            f"{base_url}?page={pagination.next_num}" if pagination.has_next else None
        ),
    }


def user_to_dict(user):
    return {"id": user.id, "username": user.username, "email": user.email}

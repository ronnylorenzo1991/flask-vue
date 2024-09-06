from app.models.role_model import Role
from app.models.permission_model import Permission
from app import db
from app.forms.role_form import RoleForm
from flask import jsonify, request, json
from flask_jwt_extended import jwt_required
from sqlalchemy import asc, desc


@jwt_required()
def all():
    current_page = request.args.get("page", 1, type=int)
    per_page = request.args.get("perPage", 10, type=int)

    # Filters
    search_name = request.args.get("name", "", type=str)
    sort_by = request.args.get("sortBy", "id", type=str)
    sort_order = request.args.get("sortDir", "desc", type=str)

    query = Role.query
    if search_name:
        query = query.filter(Role.name.like(f"%{search_name}%"))
    
    if sort_by in ["name", "id"]:
        if sort_order == "desc":
            query = query.order_by(desc(getattr(Role, sort_by)))
        else:
            query = query.order_by(asc(getattr(Role, sort_by)))

    pagination = query.paginate(page=current_page, per_page=per_page)
    data = get_pagination(pagination, current_page, per_page)
    return jsonify(data)


@jwt_required()
def create():
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data)


        db.session.add(role)
        db.session.commit()

        return (
            jsonify(
                {"message": "Role created successfully", "role": item_to_dic(role)}
            ),
            200,
        )
    else:
        return jsonify({"errors": form.errors}), 422


@jwt_required()
def update(id):
    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)

    if form.validate_on_submit():
        role.name = form.name.data
        db.session.commit()

        return (
            jsonify(
                {"message": "Role updated successfully", "role": item_to_dic(role)}
            ),
            200,
        )
    else:
        return jsonify({"errors": form.errors}), 422


@jwt_required()
def delete(id):
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    return (
        jsonify({"message": "Role removed successfully"}),
        200,
    )

@jwt_required()
def toggle_permission(id):
    request_data = json.loads(request.data)
    role = Role.query.get_or_404(id)
    permission = Permission.query.filter(Permission.name.like(f"%{request_data["permission_name"]}%")).first()
    toggle = request_data["permission_value"]
    
    if toggle == "true":
        role.permissions.append(permission)
    else:
        role.permissions.remove(permission)    
        
    db.session.commit()
    return (
        jsonify({"message": "Permission updated successfully"}),
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
        "items": [
            item_to_dic(item)
            for item in pagination.items
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


def item_to_dic(item):
    return {"id": item.id, "name": item.name, "permissions": 
        [{"id":permission.id, "name":permission.name, "display_name": permission.display_name, "module_name":permission.module_name} for permission in item.permissions],}

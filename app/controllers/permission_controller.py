from app.models.permission_model import Permission
from app import db
from app.forms.permission_form import PermissionForm
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy import asc, desc


@jwt_required()
def all():
    current_page = request.args.get("page", 1, type=int)
    per_page = request.args.get("perPage", 10, type=int)

    # Filters
    search_name = request.args.get("name", "", type=str)
    search_display_name = request.args.get("display_name", "", type=str)
    search_module_name = request.args.get("module_name", "", type=str)
    sort_by = request.args.get("sortBy", "id", type=str)
    sort_order = request.args.get("sortDir", "desc", type=str)

    query = Permission.query
    if search_name:
        query = query.filter(Permission.name.like(f"%{search_name}%"))
    if search_display_name:
        query = query.filter(Permission.display_name.like(f"%{search_display_name}%"))
    if search_display_name:
        query = query.filter(Permission.module_name.like(f"%{search_module_name}%"))
    
    if sort_by in ["name", "id"]:
        if sort_order == "desc":
            query = query.order_by(desc(getattr(Permission, sort_by)))
        else:
            query = query.order_by(asc(getattr(Permission, sort_by)))

    pagination = query.paginate(page=current_page, per_page=per_page)
    data = get_pagination(pagination, current_page, per_page)
    return jsonify(data)


@jwt_required()
def create():
    form = Permission()
    if form.validate_on_submit():
        permission = Permission(name=form.name.data, display_name=form.display_name.data, module_name=form.module_name.data)


        db.session.add(permission)
        db.session.commit()

        return (
            jsonify(
                {"message": "Permission created successfully", "permission": item_to_dic(permission)}
            ),
            200,
        )
    else:
        return jsonify({"errors": form.errors}), 422


@jwt_required()
def update(id):
    permission = Permission.query.get_or_404(id)
    form = PermissionForm(obj=permission)

    if form.validate_on_submit():
        permission.name = form.name.data
        permission.display_name = form.display_name.data
        permission.module_name = form.module_name.data
        db.session.commit()

        return (
            jsonify(
                {"message": "permission updated successfully", "permission": item_to_dic(permission)}
            ),
            200,
        )
    else:
        return jsonify({"errors": form.errors}), 422


@jwt_required()
def delete(id):
    permission = Permission.query.get_or_404(id)
    db.session.delete(permission)
    db.session.commit()
    return (
        jsonify({"message": "permission removed successfully"}),
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
    return {"id": item.id, "name": item.name, "display_name": item.display_name, "module_name": item.module_name, }

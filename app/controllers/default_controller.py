from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.models.role_model import Role
from app.models.permission_model import Permission
from ast import literal_eval


@jwt_required()
def get_lists():
    list_requested = literal_eval(request.args.get("lists", "[]", type=str))
    response = {}

    if "roles" in list_requested:
        response["roles"] = []
        roles = Role.query.all()
        for role in roles:
            response["roles"].append(item_to_dic(role, ["id", "name"]))
    if "permissions" in list_requested:
        response["permissions"] = []
        permissions = Permission.query.all()
        for permission in permissions:
            response["permissions"].append(item_to_dic(permission, ["id", "name", "display_name", "module_name"]))

    return jsonify(response)


def item_to_dic(item, keys):
    new_item = {}
    for key in keys:
        new_item[key] = getattr(item, key)

    return new_item

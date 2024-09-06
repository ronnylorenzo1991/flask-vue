from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.models.role_model import Role
from app.models.permission_model import Permission
from app.models.user_model import User
import random


@jwt_required()
def get_stats():
    roles_qty = Role.query.count()
    permissions_qty = Permission.query.count()
    users_qty = User.query.count()
    return jsonify(
        {
            "roles_qty": roles_qty,
            "permissions_qty": permissions_qty,
            "users_qty": users_qty,
        }
    )


@jwt_required()
def get_totals():
    by = request.args.get("by", "week", type=str)
    roles_count = [0] * 7
    permissions_count = [0] * 7
    users_count = [0] * 7

    for day in range(6):
        roles_count[random.randint(0, 6)] = random.randint(0, 100)
        permissions_count[random.randint(0, 6)] = random.randint(0, 100)
        users_count[random.randint(0, 6)] = random.randint(0, 100)

    return jsonify(
        {
            "roles_count": roles_count,
            "permissions_count": permissions_count,
            "users_count": users_count,
            "labels": get_labels(by),
        }
    )


def get_labels(by):
    labels = {"week": ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]}
    return labels[by]

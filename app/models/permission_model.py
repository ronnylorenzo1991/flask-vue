from app.extensions import db
from app.models.permission_roles_model import PermissionRoles

class Permission(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    display_name = db.Column(db.String(100), unique=True, nullable=False)
    module_name = db.Column(db.String(100), nullable=False)

    roles = db.relationship("Role", secondary=PermissionRoles.__table__, back_populates="permissions")


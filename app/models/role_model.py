from app.extensions import db
from app.models.user_role_model import UserRole
from app.models.permission_model import Permission
from app.models.permission_roles_model import PermissionRoles


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    db.Column('created_at', db.DateTime, default=db.func.current_timestamp()),
    db.Column('updated_at', db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    users = db.relationship("User", secondary=UserRole.__table__, back_populates="roles")
    permissions = db.relationship("Permission", secondary=PermissionRoles.__table__, back_populates="roles")
    def has_permission(self, permission):
        return bool(
            Permission.query
            .join(Role.permissions)
            .filter(Role.id == self.id)
            .filter(Permission.name == permission)
            .count() == 1
        )
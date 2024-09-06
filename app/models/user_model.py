from app.extensions import db
from app import login_manager
from flask_login import UserMixin
from app.models.role_model import Role
from app.models.user_role_model import UserRole


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    db.Column("created_at", db.DateTime, default=db.func.current_timestamp()),
    db.Column(
        "updated_at",
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    roles = db.relationship("Role", secondary=UserRole.__table__, back_populates="users")

    def has_role(self, role):
        return bool(
            Role.query.join(Role.users)
            .filter(User.id == self.id)
            .filter(Role.name == role)
            .count()
            == 1
        )

    def get_roles(self):
        roles = []
        for role in self.roles:
            roles.append(role.name)
            
        return roles
    
    def get_permissions(self):
        permissions = []
        for role in self.roles:
            for permission in role.permissions:
                permissions.append(permission.name)
            
        return permissions
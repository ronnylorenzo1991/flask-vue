from app.extensions import db


class PermissionRoles(db.Model):
    __tablename__ = "permission_roles"
    id = db.Column(db.Integer, primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey("permissions.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    

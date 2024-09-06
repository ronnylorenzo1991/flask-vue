from flask_seeder import Seeder
from app.models.permission_model import Permission
from app.models.role_model import Role


# All seeders inherit from Seeder
class PermissionSeeder(Seeder):
    # run() will be called by Flask-Seeder
    def run(self):
        #     # Create a new Faker and tell it how to create User objects
        admin_role = Role.query.filter_by(name="admin").first()
        permissions = [
            # Menu
            {
                "name": "menu_dashboard",
                "display_name": "dashboard",
                "module_name": "menu",
            },
            {
                "name": "menu_roles",
                "display_name": "Listar Roles",
                "module_name": "menu",
            },
            {
                "name": "menu_users",
                "display_name": "Listar Usuarios",
                "module_name": "menu",
            },
            {
                "name": "menu_permissions",
                "display_name": "Listar Permisos",
                "module_name": "menu",
            },
            # Security Roles
            {
                "name": "security_roles_create",
                "display_name": "Crear Roles",
                "module_name": "security",
            },
            {
                "name": "security_roles_edit",
                "display_name": "Editar Roles",
                "module_name": "security",
            },
            {
                "name": "security_roles_remove",
                "display_name": "Eliminar Roles",
                "module_name": "security",
            },
            # Security Users
            {
                "name": "security_users_create",
                "display_name": "Crear Usuarios",
                "module_name": "security",
            },
            {
                "name": "security_users_edit",
                "display_name": "Editar Usuarios",
                "module_name": "security",
            },
            {
                "name": "security_users_remove",
                "display_name": "Eliminar Usuarios",
                "module_name": "security",
            },
            # Security Permissions
            {
                "name": "security_permissions_create",
                "display_name": "Crear Permisos",
                "module_name": "security",
            },
            {
                "name": "security_permissions_edit",
                "display_name": "Editar Permisos",
                "module_name": "security",
            },
            {
                "name": "security_permissions_remove",
                "display_name": "Eliminar Permisos",
                "module_name": "security",
            },
        ]

        for permission in permissions:
            permission_obj = Permission(**permission)
            print("Adding permission: %s" % permission_obj.name)
            self.db.session.add(permission_obj)
            admin_role.permissions.append(permission_obj)

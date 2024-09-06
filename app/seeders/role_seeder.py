from flask_seeder import Seeder
from app.models.role_model import Role


# All seeders inherit from Seeder
class RoleSeeder(Seeder):
    # run() will be called by Flask-Seeder
    def run(self):
    #     # Create a new Faker and tell it how to create User objects
        roles = [
            {
                "id": 1,
                "name": "admin",
            },
            {
                "id": 2,
                "name": "cliente",
            },
        ]

        for role in roles:
            role_obj = Role(**role)
            print("Adding role: %s" % role_obj.name)
            self.db.session.add(role_obj)
            
        
from flask_seeder import Seeder, Faker, generator
from app.models.user_model import User
from app.models.role_model import Role
from app.extensions import bcrypt


# All seeders inherit from Seeder
class UserSeeder(Seeder):
    # run() will be called by Flask-Seeder
    def run(self):
        admin_role = Role.query.filter_by(name="admin").first()
        client_role = Role.query.filter_by(name="client").first()
        # Create a new Faker and tell it how to create User objects
        default_password = "secret"
        faker = Faker(
            cls=User,
            init={
                "username": generator.Name(),
                "email": generator.Email(),
                "password": bcrypt.generate_password_hash(default_password).decode(
                    "utf-8"
                ),
            },
        )
        dev_user = User(
            username="desarrollo",
            email="desarrollo@gmail.com",
            password=bcrypt.generate_password_hash(default_password).decode("utf-8"),
        )
        self.db.session.add(dev_user)
        dev_user.roles.append(admin_role)

        # Create 15 users
        for user in faker.create(15):
            print("Adding user: %s" % user.username)
            self.db.session.add(user)
            user.roles.append(admin_role)

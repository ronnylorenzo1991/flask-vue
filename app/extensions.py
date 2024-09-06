from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_seeder import FlaskSeeder

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
jwt = JWTManager()
seeder = FlaskSeeder()
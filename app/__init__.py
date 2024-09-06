from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.extensions import db, migrate, bcrypt, login_manager, jwt, seeder
from app.routes.base_routes import bp
from app.routes.user_routes import user_bp
from app.routes.role_routes import role_bp
from app.routes.dashboard_routes import dashboard_bp

login_manager.login_view = "main.login"


def create_app():
    app = Flask(
        __name__,
        static_folder="./frontend/dist/assets",
        template_folder="./frontend/dist",
    )
    app.config.from_object(Config)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)
    seeder.init_app(app, db)
    with app.app_context():
        app.register_blueprint(bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(role_bp)
        app.register_blueprint(dashboard_bp)

    return app

from flask import Flask
from config import Config
from .extensions import db, jwt, login_manager
from app.controllers.auth_controller import auth_bp
from app.controllers.user_controller import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/user")

    return app
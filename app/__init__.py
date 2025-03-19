from flask import Flask
from config import Config
from .extensions import db, jwt, login_manager
from app.controllers.auth_controller import bp as auth_bp
from app.controllers.user_controller import bp as user_bp
from app.controllers.bike_controller import bp as bike_bp
from app.controllers.chain_controller import bp as chain_bp
from app.controllers.frame_controller import bp as frame_bp
from app.controllers.frame_finish_controller import bp as ff_bp
from app.controllers.frame_type_controller import bp as ft_bp
from app.controllers.product_controller import bp as product_bp
from app.controllers.product_type_controller import bp as pt_bp
from app.controllers.rim_controller import bp as rim_bp
from app.controllers.wheel_controller import bp as wheel_bp
from app.controllers.valid_combinations_controller import bp as vc_bp
from app.controllers.cart_controller import bp as cart_bp


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
    app.register_blueprint(bike_bp, url_prefix="/bike")
    app.register_blueprint(chain_bp, url_prefix="/chain")
    app.register_blueprint(frame_bp, url_prefix="/frame")
    app.register_blueprint(ff_bp, url_prefix="/frame-finish")
    app.register_blueprint(ft_bp, url_prefix="/frame-type")
    app.register_blueprint(product_bp, url_prefix="/product")
    app.register_blueprint(pt_bp, url_prefix="/product-type")
    app.register_blueprint(rim_bp, url_prefix="/rim")
    app.register_blueprint(wheel_bp, url_prefix="/wheel")
    app.register_blueprint(vc_bp, url_prefix="/valid-combinations")
    app.register_blueprint(cart_bp, url_prefix="/cart")

    return app

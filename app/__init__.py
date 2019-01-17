# coding=utf-8
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager
)
from flask_login import LoginManager
from flask_recaptcha import ReCaptcha
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
recaptcha = ReCaptcha()
socketio = SocketIO()
jwt = JWTManager()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'plz login to access'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    recaptcha.init_app(app)
    socketio.init_app(app)
    jwt.init_app(app)
    # pagedown = PageDown(app)
    from .api import api as api_blueprint
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app

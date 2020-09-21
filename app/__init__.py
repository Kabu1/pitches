from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # 

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Setting up configuration
    app.config.from_object(DevConfig)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

    return app

    
    
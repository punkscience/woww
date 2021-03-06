# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import app_config

# Init a database
db = SQLAlchemy()

def create_app( config_name ):
    app = Flask(__name__, instance_relative_config=True)

   # Load the config file -- this has to happen before we init the db/app below
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    loginMgr = LoginManager()
    loginMgr.login_view = 'auth.login'
    loginMgr.init_app( app )

    from .models import User

    @loginMgr.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # with app.app_context():
    #     db.create_all()  # Create sql tables for our data models

    return app





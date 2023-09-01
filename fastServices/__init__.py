from fastServices.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()
def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from fastServices.routes.user import users

    app.register_blueprint(users)

    return app


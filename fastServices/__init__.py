import os

from flask_sqlalchemy.record_queries import get_recorded_queries
from sqlalchemy import engine

from fastServices.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from flask import Flask




class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate(directory= "migrations")

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db = db)

    from fastServices.models import (direccion, foto_solicitud, localidad, presupuesto, profesion, solicitud, usuario,
                                     servicio, horario_presupuesto)



    from fastServices.controller.user import users
    from fastServices.controller.direccion_controller import direccion_controller
    from fastServices.controller.profesion_controller import profesion_controller


    app.register_blueprint(users)
    app.register_blueprint(direccion_controller)
    app.register_blueprint(profesion_controller)

    return app

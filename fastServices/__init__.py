import os

from flask_sqlalchemy.record_queries import get_recorded_queries
from sqlalchemy import engine

from fastServices.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate(directory= "migrations")
bcrypt = Bcrypt()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db = db)
    bcrypt.init_app(app)
    cors.init_app(app)

    from fastServices.models import (direccion, foto_solicitud, localidad, presupuesto, profesion, solicitud, usuario,
                                     servicio, horario_presupuesto)




    from fastServices.controller.direccion_controller import direccion_controller
    from fastServices.controller.profesion_controller import profesion_controller
    from fastServices.controller.usuario_controller import usuario_controller



    app.register_blueprint(direccion_controller)
    app.register_blueprint(profesion_controller)
    app.register_blueprint(usuario_controller)

    return app

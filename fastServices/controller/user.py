from flask.blueprints import Blueprint

users = Blueprint("users",__name__)


@users.route("/users/create")
def create():
    return "<h1>Hola mundo</h1>"
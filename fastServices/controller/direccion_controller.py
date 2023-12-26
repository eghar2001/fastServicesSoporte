from flask import jsonify
from flask.blueprints import  Blueprint
import asyncio

direccion_controller = Blueprint("direccion_controller", __name__)

@direccion_controller.route("/cliente/<user_id>")
def get_solicitudes_cliente(user_id:int):
    data = {
        "nombre":"Nahuel",
        "apellido":"Coronel",
        "dni":43840925
    }
    return jsonify(data),200


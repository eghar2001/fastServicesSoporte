from flask import Blueprint, jsonify

from fastServices.negocio import profesion_negocio

profesion_controller = Blueprint("profesion_controller",__name__)

@profesion_controller.route("/profesiones")
def get_profesiones():
    profesiones = profesion_negocio.get_profesiones()
    profesiones_dict = [prof.toDict() for prof in profesiones]
    if profesiones:
        return jsonify(profesiones_dict),200
    return jsonify({"mensaje":"No hay profesiones registradas"}),404
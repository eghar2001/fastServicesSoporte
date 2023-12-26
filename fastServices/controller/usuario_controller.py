from flask import Blueprint, jsonify

from fastServices.negocio.usuario_negocio import UsuarioNegocio

usuario_controller = Blueprint("usuario_controller",__name__)


usuario_negocio = UsuarioNegocio()
@usuario_controller.route("/listaUsuarios")
def get_usuarios():
    try:
        usuarios = usuario_negocio.get_usuarios()
        usuarios_dict = [user.toDict() for user in usuarios]
        return jsonify(usuarios),200
    except Exception:
        return jsonify({"message":"Error al obtener los usuarios"}),500


@usuario_negocio.route("listaUsuarios/<id>")
def get_usuario(id:int):
    try:
        usuario= usuario_negocio.get_usuario(id)
        if not usuario:
            return jsonify({"message":"No se encontró el usuario"}),404
        return usuario
    except Exception:
        return jsonify({"message": "Hubo un problema al encontrar usuario"}), 500
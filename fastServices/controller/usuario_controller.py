from flask import Blueprint, jsonify, request

from fastServices.models.direccion import Direccion
from fastServices.models.localidad import Localidad
from fastServices.models.profesion import Profesion
from fastServices.models.usuario import Usuario
from fastServices.negocio.usuario_negocio import UsuarioNegocio, MailRegistradoException
from fastServices import bcrypt
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


@usuario_controller.route("/listaUsuarios/<int:id>")
def get_usuario(id:int):
    try:
        usuario= usuario_negocio.get_usuario(id)
        if not usuario:
            return jsonify({"message":"No se encontró el usuario"}),404
        return usuario
    except Exception:
        return jsonify({"message": "Hubo un problema al encontrar usuario"}), 500


@usuario_controller.route("/usuario/login")
def login():
    return jsonify({"message": "Usuario logueado con exito!"}),200

@usuario_controller.route("/usuario/register",methods=["POST"])
def register():
    data = request.get_json()
    print(data)
    password_hash = bcrypt.generate_password_hash(data["contrasena"]).decode('utf-8')
    user = Usuario(
        nombre=data["nombre"],
        apellido=data["apellido"],
        email=data["email"],
        contrasenia=password_hash,
        fecha_nacimiento=data["fechaNacimiento"],
        telefono=data["telefono"],
        es_prestador=data["esPrestador"]
    )
    especialidades_dict = data["especialidades"]
    direcciones_dict = data["direcciones"]

    especialidades = []
    direcciones=[]
    localidades = []
    if especialidades_dict:
        especialidades = [
            Profesion(nombre = prof) for prof in especialidades_dict
        ]
    if direcciones_dict:
        for dir in direcciones_dict:

            piso = dir["piso"] if "piso" in dir else None
            dpto = dir["dpto"] if "dpto" in dir else None
            cod_postal = int(dir["codPostal"])
            direccion = Direccion(
               calle=dir["calle"],
               numero=dir["numero"],
               piso= piso,
               dpto=dpto,
               cod_postal=cod_postal
            )
            localidad = Localidad(
                cod_postal = cod_postal,
                nombre = dir["ciudad"],
                provincia = dir["provincia"]
            )
            direcciones.append(direccion)
            localidades.append(localidad)

        try:
            usuario_negocio.register_user(user, direcciones, localidades, especialidades)
        except MailRegistradoException:
            return jsonify({"message":"El mail ya está registrado"}),400
        return jsonify({"message": "El usuario se ha creado con exito!"}),200






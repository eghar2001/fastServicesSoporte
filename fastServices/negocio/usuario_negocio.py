from typing import List, Set

from fastServices import db
from fastServices.data.localidad_data import LocalidadData
from fastServices.data.profesion_data import ProfesionData
from fastServices.data.usuario_data import UsuarioData
from fastServices.models.direccion import Direccion
from fastServices.models.localidad import Localidad
from fastServices.models.profesion import Profesion
from fastServices.models.usuario import Usuario


class UsuarioNegocio:
    def __init__(self):
        self.__usuario_data = UsuarioData()
        self.__localidad_data = LocalidadData()
        self.__profesion_data = ProfesionData()

    def get_usuarios(self):
        return self.__usuario_data.get_usuarios()

    def get_usuario(self, id: int):
        return self.__usuario_data.get_usuario(id)

    def register_user(self, user: Usuario, direcciones: List[Direccion] = [], localidades: List[Localidad] = [],
                      especialidades: List[Profesion] = []):

        # Filtramos localidades y buscamos las localidades nuevas
        cod_postales = [dir.cod_postal for dir in direcciones]
        localidades_registradas = self.__localidad_data.get_localidades_existentes(cod_postales)
        localidades_nuevas:Set[Localidad] = set(filter(lambda loc: loc not in localidades_registradas, localidades))
        for loc in localidades_nuevas:
            loc.nombre = loc.nombre.capitalize()
            loc.provincia = loc.provincia.capitalize()

        try:
            db.session.add_all(localidades_nuevas)
        except Exception:
            db.session.rollback()
            raise Exception("No se pudieron crear las localidades")

        # Registramos el usuario
        user_registrado = self.__usuario_data.get_usuario_by_email(user.email)
        if user_registrado:
            raise MailRegistradoException("El mail se encuentra registrado")
        try:
            db.session.add(user)
            db.session.flush()
            db.session.refresh(user)
        except Exception:
            db.session.rollback()
            raise Exception("Error al crear el usuario")

        #Registramos las direcciones
        for dir in direcciones:
            dir.calle = dir.calle.capitalize()
            dir.dpto = dir.dpto.capitalize() if dir.dpto else None
        direcciones_set = set(direcciones)
        for dir in direcciones_set:
            dir.id_usuario = user.id
        try:
            db.session.add_all(direcciones_set)
        except Exception:
            db.session.rollback()
            raise Exception("Error al agregar direcciones")


        #Registramos las especialidades
        if user.es_prestador and especialidades:
            #POnemos todos los nombres en minuscula
            for esp in especialidades:
                esp.nombre = esp.nombre.lower()

            #Buscamos las profesiones cuyos nombres ya esten registrados
            nombres = [esp.nombre for esp in especialidades]
            profesiones_existentes = self.__profesion_data.get_profesiones_existentes(nombres = nombres)

            #Aquellas especialidades registradas, las sustituimos por la entidad de la bbdd que se tiene el base de datos
            for prof in profesiones_existentes:
                i = 0
                while especialidades[i] != prof and i < len(especialidades):
                    i +=1
                if especialidades[i] == prof:
                    especialidades[i] = prof
            user.profesiones = especialidades


        db.session.commit()
        print("Usuario registrado con exito!")


class MailRegistradoException(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

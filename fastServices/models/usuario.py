from typing import List, Set

from fastServices import db
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from sqlalchemy import Integer, String, Boolean,DateTime,LargeBinary

from fastServices.models.direccion import Direccion
from fastServices.models.prestador_profesiones import prestador_profesiones


class Usuario(db.Model):

    __tablename__ = "usuarios"

    id:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        autoincrement = True
    )
    nombre:Mapped[str]  = mapped_column(
        String(40),
        nullable = False
    )
    apellido:Mapped[str]  = mapped_column(
        String(40),
        nullable = False
    )
    email:Mapped[str]  = mapped_column(
        String(255),
        nullable = False,
        #REVISAR
        unique = True
    )

    contrasenia:Mapped[str]  = mapped_column(
        String(250),
        nullable = False
    )

    fecha_nacimiento:Mapped[datetime]  = mapped_column(
        DateTime,
        nullable = False
    )

    telefono:Mapped[str]  = mapped_column(
        String(20),
        nullable = False
    )

    es_prestador:Mapped[bool]  = mapped_column(
        Boolean,
        nullable = False
    )



    foto_perfil:Mapped[str]  = mapped_column(
        String(255),
        nullable = True
    )

    foto:Mapped[bytes]  = mapped_column(
        LargeBinary,
        nullable = True
    )


    direcciones: Mapped[Set["Direccion"]] = relationship(
        "Direccion",
        backref="usuario"
    )

    #Profesiones
    #EXCLUSIVO PARA PRESTADORES
    profesiones: Mapped[List["Profesion"]] = relationship(
        secondary=prestador_profesiones,
        backref="prestadores"
    )
    def toDict(self):
        usuario_dict = {
            "id":id,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "email":self.email,
            "contrasenia":self.contrasenia,
            "fecha_nacimiento":self.fecha_nacimiento,
            "telefono":self.telefono,
            "es_prestador": self.esPrestador,
            "fotoPerfil":self.fotoPerfil,
            "foto": self.foto,

        }


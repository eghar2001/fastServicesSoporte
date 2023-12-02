from fastServices import db
from fastServices.models.PrestadorProfesiones import prestador_profesiones

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String

from fastServices.models.Usuario import Usuario


class Profesion(db.Model):

    __tablename__="profesiones"

    id:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        autoincrement = True
    )

    nombre:Mapped[str]  = mapped_column(
        String(255),
        nullable = False
    )


    """
    Lo ideal seria que el prestador tenga mapeada sus profesiones, pero 
    como la entidad Usuario puede ser Prestador o simple usuario, un simple usuario
    tendria una propiedad "profesiones" que no le pertenece
    """
    prestadores:Mapped[set[Usuario]] = relationship(secondary=prestador_profesiones)
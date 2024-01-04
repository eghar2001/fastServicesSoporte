from fastServices import db
from fastServices.models.prestador_profesiones import prestador_profesiones

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String



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

    def toDict(self):
        dict = {
            "id":self.id,
            "nombre":self.nombre
        }
        return dict

    def __eq__(self, other):
        if not isinstance(other, Profesion):
            return False
        return self.nombre == other.nombre
    """
    Lo ideal seria que el prestador tenga mapeada sus profesiones, pero 
    como la entidad Usuario puede ser Prestador o simple usuario, un simple usuario
    tendria una propiedad "profesiones" que no le pertenece
    """
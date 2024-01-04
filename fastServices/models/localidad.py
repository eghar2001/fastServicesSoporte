from sqlalchemy import Integer, String

from fastServices import db
from sqlalchemy.orm import mapped_column,Mapped
class Localidad(db.Model):
    __tablename__ = "localidades"

    cod_postal:Mapped[int] = mapped_column(
        Integer,
        primary_key = True
    )

    nombre:Mapped[str] = mapped_column(
        String(150),
        nullable = False
    )
    provincia:Mapped[str]  = mapped_column(
        String(150),
        nullable = False
    )

    def __eq__(self,other):
        if not isinstance(other, Localidad):
            return False
        return other.cod_postal == self.cod_postal

    def __hash__(self):
        return hash(self.cod_postal)
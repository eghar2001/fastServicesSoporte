from sqlalchemy import Integer, String

from fastServices import db
from sqlalchemy.orm import mapped_column,Mapped
class Localidad(db.Model):
    __tablename__ = "localidades"

    cod_postal:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        autoincrement =True
    )

    nombre:Mapped[str] = mapped_column(
        String(150),
        nullable = False
    )
    provincia:Mapped[str]  = mapped_column(
        String(150),
        nullable = False
    )

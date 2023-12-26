from sqlalchemy import ForeignKey, Integer, DateTime, String

from fastServices import db
from sqlalchemy.orm import mapped_column,Mapped
from datetime import datetime
class Solicitud(db.Model):
    """Solicitud """


    __tablename__="solicitudes"


    id:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        autoincrement = True
    )

    fechahora:Mapped[datetime]  = mapped_column(
        DateTime,
        nullable = False
    )

    titulo:Mapped[str]  = mapped_column(
        String(45),
        nullable = False
    )

    descripcion:Mapped[str]  = mapped_column(
        String(255),
        nullable = False
    )

    estado:Mapped[str]  = mapped_column(
        String(20),
        nullable = False
    )


    id_direccion:Mapped[int] = mapped_column(
        Integer,
        nullable = False
    )

    id_profesion:Mapped[int] = mapped_column(
        Integer,
        ForeignKey("profesiones.id"),
        nullable = False
    )

from sqlalchemy import ForeignKey, Integer, DateTime, String, ForeignKeyConstraint

from fastServices import db
from sqlalchemy.orm import mapped_column,Mapped
from datetime import datetime
class Servicio(db.Model):
    """Entidad que representa un servicio en el modelo"""


    __tablename__ = "servicios"


    #Lo siguiente es una clave foranea compuesta a presupuesto
    ###
    id_solicitud:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        autoincrement = False
    )

    id_prestador:Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        nullable = False
    )



    fechahora:Mapped[datetime]  = mapped_column(
        DateTime,
        nullable = False
    )

    estado:Mapped[str]  = mapped_column(
        String(45),
        nullable = False
    )

    resenia:Mapped[int] = mapped_column(
        Integer,
        nullable = True
    )

    __table_args__ = (
        ForeignKeyConstraint(
            [ "id_prestador","id_solicitud"],
            ["presupuestos.id_prestador","presupuestos.id_solicitud"]
        ),
    )

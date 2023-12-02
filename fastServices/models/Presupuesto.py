from sqlalchemy import ForeignKey, Integer, String, Float

from fastServices import db
from sqlalchemy.orm import mapped_column, Mapped


class Presupuesto(db.Model):
    __tablename__ = "presupuestos"

    id_solicitud: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("solicitudes.id"),
        primary_key=True
    )
    id_prestador: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("usuarios.id"),
        primary_key= True
    )
    materiales: Mapped[str] = mapped_column(
        String(255),
        nullable = False
    )

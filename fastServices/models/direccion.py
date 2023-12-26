from sqlalchemy import Integer, String, ForeignKey

from fastServices import db
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

class Direccion(db.Model):
    """Clase que representa la direccion en la que se encuentra un usuario del sistema"""
    __tablename__ = "direcciones"

    id:Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    calle:Mapped[str] = mapped_column(
        String(45),
        nullable=False
    )
    numero:Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )
    piso:Mapped[Optional[str]] = mapped_column(
        String(10),
        nullable=True
    )
    dpto:Mapped[Optional[str]] = mapped_column(
        String(10),
        nullable=True
    )


    id_usuario:Mapped[int] = mapped_column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable = False

    )

    cod_postal:Mapped[int] = mapped_column(
        Integer,
        ForeignKey("localidades.cod_postal"),
        nullable = False
    )
from sqlalchemy import  Integer, LargeBinary, String, ForeignKey

from fastServices import db
from sqlalchemy.orm import mapped_column,Mapped
class FotoSolicitud(db.Model):
    """Entidad que contene la foto de una solicitud"""

    __tablename__ = "fotos_solicitud"

    id:Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    foto:Mapped[bytes]  = mapped_column(
        LargeBinary,
        nullable = False
    )

    nombre:Mapped[str]  = mapped_column(
        String(50),
        nullable = False
    )

    tipo:Mapped[str]  = mapped_column(
        String(45),
        nullable = False
    )


    #FK --> Solicitud
    id_solicitud:Mapped[int] = mapped_column(
        Integer,
        ForeignKey("solicitudes.id"),
        nullable = False
    )

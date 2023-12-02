from fastServices import db
from sqlalchemy.orm import mapped_column,Mapped
from datetime import datetime
from sqlalchemy import Integer, String, Boolean,DateTime,LargeBinary
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

    esPrestador:Mapped[bool]  = mapped_column(
        Boolean,
        nullable = False
    )

    fotoPerfil:Mapped[str]  = mapped_column(
        String(255),
        nullable = True
    )

    foto:Mapped[bytes]  = mapped_column(
        LargeBinary,
        nullable = True
    )


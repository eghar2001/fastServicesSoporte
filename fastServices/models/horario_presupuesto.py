from sqlalchemy import Integer, ForeignKeyConstraint, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from fastServices import db

class HorarioPresupuesto(db.Model):
    """Entidad intermedia entre horarios y un presupuesto"""

    __tablename__= "horarios_presupuesto"



    id_solicitud:Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    id_prestador:Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    horario:Mapped[datetime] = mapped_column(
        DateTime,
        primary_key=True
    )

    __table_args__ = (
        ForeignKeyConstraint(
            ["id_prestador","id_solicitud"],
            ["presupuestos.id_prestador", "presupuestos.id_solicitud"],
            onupdate="CASCADE",
            ondelete="CASCADE"
        ),
    )
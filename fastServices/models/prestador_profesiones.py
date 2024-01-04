from sqlalchemy import Column, ForeignKey

from fastServices import db

"""Mapeo realizado desde Profesion"""
prestador_profesiones = db.Table(
    "prestador_profesiones",
    Column(
        "id_prestador", ForeignKey("usuarios.id",onupdate="CASCADE", ondelete="CASCADE"), primary_key = True    ),
    Column(
        "id_profesion", ForeignKey("profesiones.id",onupdate="CASCADE", ondelete="CASCADE"),primary_key=True
    )
)
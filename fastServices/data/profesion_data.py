from fastServices.models.profesion import Profesion


def get_profesiones():
    profesiones = Profesion.query.all()
    return profesiones

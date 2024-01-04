from typing import List

from fastServices.models.profesion import Profesion

class ProfesionData:
    def get_profesiones(self):
        """Retorna todas las profesiones registradas en la base de datos"""
        profesiones = Profesion.query.all()
        return profesiones

    def get_profesion(self, id:int):
        profesion = Profesion.query.get(id)
        return profesion

    def get_profesiones_existentes(self, nombres: List[str]):
        profesiones_encontradas = Profesion.query.filter(Profesion.nombre.in_(nombres)).all()
        return profesiones_encontradas

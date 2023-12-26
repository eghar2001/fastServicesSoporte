from fastServices.models.profesion import Profesion

class ProfesionData:
    def get_profesiones(self):
        profesiones = Profesion.query.all()
        return profesiones

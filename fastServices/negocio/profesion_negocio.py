from fastServices.data.profesion_data import ProfesionData

class ProfesionNegocio:
    def __init__(self):
        self.__profesion_data = ProfesionData()
    def get_profesiones(self):
        return self.__profesion_data.get_profesiones()
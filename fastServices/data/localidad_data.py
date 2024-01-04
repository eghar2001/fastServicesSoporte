from typing import List
from fastServices import db
from fastServices.models.localidad import Localidad


class LocalidadData():
    def get_localidad(self, cod_postal:str):
        """Busca un codigo postal en la BBDD y lo retorna si existe, si no
        retorna null"""
        return Localidad.query.get(cod_postal)

    def get_localidades_existentes(self, cod_postales:List[str]):
        """De un grupo de codigo postales, retorna aquellas localidades
        cuyo codigo postal este registrado"""
        cod_postales = set(cod_postales)

        localidades_existentes =  []
        for cod in cod_postales:
            loc = self.get_localidad(cod)
            if loc:
                localidades_existentes.append(loc)

        return localidades_existentes



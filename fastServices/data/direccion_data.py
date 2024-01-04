from fastServices.models.direccion import Direccion


class DireccionData:

    def get_direcciones(self):
        """Retorna todas las direcciones existentes en la base de datos"""
        return Direccion.query.all()

    def get_direcciones_user(self, user_id:int):
        """Retorna todas las direcciones existentes de un usuario dado su id"""
        return Direccion.query.filter(Direccion.id_usuario == user_id).order_by(Direccion.cod_postal.desc()).all()



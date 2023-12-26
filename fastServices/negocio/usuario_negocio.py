from fastServices.data.usuario_data import UsuarioData


class UsuarioNegocio:
    def __init__(self):
        self.__usuario_data = UsuarioData
    def get_usuarios(self):
        return self.__usuario_data.get_usuarios()

    def get_usuario(self,id: int):
        return self.__usuario_data.get_usuario(id)

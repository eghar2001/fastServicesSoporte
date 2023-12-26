from fastServices.models.usuario import Usuario


class UsuarioData:
    def get_usuarios(self):
        return Usuario.query.all()

    def get_usuario(self,id: int):
        return Usuario.query.get(id)

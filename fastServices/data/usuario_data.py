from fastServices.models.usuario import Usuario


class UsuarioData:
    def get_usuarios(self):
        """Retorna todos los usuarios registrados en la base de datos"""
        return Usuario.query.all()

    def get_usuario(self,id: int):
        """Retorna un unico usuario si existe"""
        return Usuario.query.get(id)

    def get_usuario_by_email(self,email:str):
        return Usuario.query.filter(Usuario.email == email).first()

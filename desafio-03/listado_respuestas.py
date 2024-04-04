from usuario import Usuario

class ListadoRespuestas():
    def __init__(self, respuestas:list, usuario:Usuario) -> None:
        self.respuestas = respuestas
        self.usuario = usuario
        
    def mostrar_respuesta(self) -> None:
        print(f"Las respuestas del usuario {self.usuario.correo} son:")
        print(self.respuestas)
        print('\n')

        
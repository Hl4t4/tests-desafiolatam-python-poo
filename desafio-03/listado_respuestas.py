from usuario import Usuario

class ListadoRespuestas():
    def __init__(self, respuestas:list, usuario:Usuario) -> None:
        self.respuestas = respuestas
        self.usuario = usuario
        
    def mostrar_respuestas(self):
        print(f"Las respuestas del usuario {self.usuario.nombre} son:")
        print(self.respuestas)
        
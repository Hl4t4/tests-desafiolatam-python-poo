class Alternativa():
    def __init__(self, contenido:str, ayuda="") -> None:
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self) -> None:
        print(f"La alternativa es: {self.contenido}")
        if self.ayuda != "":
            print(f"La ayuda es:\n {self.ayuda}")
        print('\n')
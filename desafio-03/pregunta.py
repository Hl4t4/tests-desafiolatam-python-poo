from alternativa import Alternativa

class Pregunta():
    def __init__(self, enunciado:str, requerida:bool, alternativas:dict, ayuda="") -> None:
        self.enunciado = enunciado
        self.requerida = requerida
        self.ayuda = ayuda
        self.__lista_de_alternativas = []
        for alternativa in alternativas:
            self.__lista_de_alternativas.append(Alternativa(alternativa["contenido"], alternativa["ayuda"]))
    
    @property
    def lista_de_alternativas(self):
        return self.__lista_de_alternativas

    def mostrar_pregunta(self):
        if self.requerida:
            print(f"La pregunta requerida")
        else:
            print(f"La pregunta no es requerida")
        print(f"La pregunta es: {self.enunciado}")
        if self.ayuda != "":
            print(f"La ayuda es:\n {self.ayuda}")
        print('\n')
        for alternativa in self.lista_de_alternativas:
            alternativa.mostrar_alternativa()
        print('\n')
        
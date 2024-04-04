from abc import ABC
from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta(ABC):
    def __init__(self, nombre:str, preguntas:dict) -> None:
        self.nombre = nombre
        self.__lista_de_preguntas = []
        self.__listados_de_respuestas = []
        for pregunta in preguntas:
            self.__lista_de_preguntas.append(Pregunta(pregunta["enunciado"], pregunta["requerida"], pregunta["alternativas"], pregunta["ayuda"]))

    @property
    def lista_de_preguntas(self):
        return self.__lista_de_preguntas

    @property
    def listados_de_respuestas(self):
        return self.__listados_de_respuestas
    
    def agregar_respuestas(self, listado_de_respuestas:ListadoRespuestas):
        self.__listados_de_respuestas.append(listado_de_respuestas)

    def mostrar_encuesta(self):
        print(f"La encuesta {self.nombre} tiene las siguientes preguntas:\n")
        for respuesta in self.lista_de_preguntas:
            respuesta.mostrar_pregunta()
        print('Y las siguientes respuestas:\n')
        for respuesta in self.listados_de_respuestas:
            respuesta.mostrar_respuesta()
        print('\n')
        
class EncuestaLimitadaEdad (Encuesta):
    def __init__(self, nombre: str, preguntas: dict, edad_minima:int, edad_maxima:int) -> None:
        super().__init__(nombre, preguntas)
        if self.comprobar_limite_edades(edad_minima, edad_maxima):
            self.edad_minima = edad_minima
            self.edad_maxima = edad_maxima    
        else:
            #En este punto se deberia pedir de nuevo los limites de edades
            self.edad_minima = edad_minima
            self.edad_maxima = edad_minima

    def agregar_respuestas(self, listado_de_respuestas:ListadoRespuestas):
        if self.comprobar_edad(listado_de_respuestas.usuario.edad):
            self.__listados_de_respuestas.append(listado_de_respuestas)

    def comprobar_edad(self, edad:int):
        return self.edad_minima >= edad >= self.edad_maxima
    
    @staticmethod
    def comprobar_limite_edades(edad_minima, edad_maxima):
        if edad_minima > edad_maxima:
            return False
        return True


class EncuestaLimitadaRegion (Encuesta):
    def __init__(self, nombre: str, preguntas: dict, lista_de_regiones:list) -> None:
        super().__init__(nombre, preguntas)
        #Falta logica de regiones validas
        self.lista_de_regiones = lista_de_regiones

    def agregar_respuestas(self, listado_de_respuestas:ListadoRespuestas):
        if self.comprobar_region(listado_de_respuestas.usuario.region):
            self.__listados_de_respuestas.append(listado_de_respuestas)

    def comprobar_region(self, region):
        return region in self.lista_de_regiones

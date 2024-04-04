from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from listado_respuestas import ListadoRespuestas
from typing import Union

class Usuario():
    def __init__(self, correo:str, edad:int, region:int) -> None:
        self.correo = correo
        self.edad = edad
        self.region = region
        
    def contestar_encuesta(self, listado_de_respuestas:list, encuesta: Union[Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion]):
        encuesta.agregar_respuestas(ListadoRespuestas(listado_de_respuestas, self))
        return encuesta
    
#Falta logica para obtener el listado de respuestas y asociarlas correctamente a las preguntas
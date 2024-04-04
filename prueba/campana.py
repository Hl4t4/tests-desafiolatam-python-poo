from datetime import date, datetime
from anuncio import Anuncio

class Campana():
    def __init__(self, nombre:str, fecha_inicio:date, fecha_termino:date, anuncio:Anuncio) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [anuncio]

    def __str__(self) -> str:
        pass
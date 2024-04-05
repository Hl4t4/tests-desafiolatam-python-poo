from datetime import date, datetime
from anuncio import Anuncio, Video, Display, Social
from typing import List, Union
from error import LargoExcedidoError

class Campana():
    def __init__(self, nombre:str, fecha_inicio:date, fecha_termino:date, anuncio:dict) -> None:
        '''Constructor de la clase Campana
        Parameters
        ----------
        self: [Campana]
            Objeto con propiedades de objeto Campana
        nombre: [str]
            Nombre para la campaña
        fecha_inicio: [date]
            Fecha de inicio de la campaña
        fecha_termino: [date]
            Fecha de termino de la campaña
        anuncio: [dict]
            Diccionario con los datos necesarios para crear un anuncio de tipo Video, Display o Social
        Returns
        ----------
        '''
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        formato = Anuncio.formato(anuncio["sub_tipo"])
        #Video es distinto porque tiene duracion y no ancho y alto
        if formato == Video:
            self.__anuncios = [formato(url_archivo = anuncio["url_archivo"], url_clic= anuncio["url_clic"], sub_tipo= anuncio["sub_tipo"], duracion= anuncio["duracion"])]
        else:
            self.__anuncios = [formato(ancho = anuncio["ancho"], alto = anuncio["alto"], url_archivo = anuncio["url_archivo"], url_clic= anuncio["url_clic"], sub_tipo= anuncio["sub_tipo"])]

    @property
    def nombre(self) -> str:
        '''getter de atributo nombre
        Parameters
        ----------
        self: [Campana]
            Objeto con propiedades de objeto Campana
        Returns
        ----------
        [int]
            Se retorna el nombre de la campaña
        '''
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre:str) -> None:
        '''setter de atributo nombre que comprueba si no sobrepasa el limite de caracteres
        Parameters
        ----------
        self: [Campana]
            Objeto con propiedades de objeto Campana
        nombre: [str]
            Nuevo nombre a modificar
        Returns
        ----------
        '''
        if len(nombre) > 250:
            raise LargoExcedidoError(nombre, 250)
        else:
            self.__nombre = nombre
    
    @property
    def fecha_inicio(self) -> date:
        '''getter de atributo fecha_inicio
        Parameters
        ----------
        self: [Campana]
            Objeto con propiedades de objeto Campana
        Returns
        ----------
        [int]
            Retorna la fecha de inicio
        '''
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio:date) -> None:
        '''setter de atributo fecha_inicio FALTA LOGICA
        Parameters
        ----------
        self: [Campana]
            Objeto con propiedades de objeto Campana
        fecha_inicio: [date]
            Fecha de inicio de la campaña
        Returns
        ----------
        '''
        self.__fecha_inicio = fecha_inicio
    
    @property
    def fecha_termino(self) -> date:
        '''getter de atributo fecha_termino
        Parameters
        ----------
        self: [Campana]
            Objeto con propiedades de objeto Campana
        Returns
        ----------
        [int]
            Retorna la fecha de termino
        '''
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino:date) -> None:
        '''setter de atributo fecha_termino FALTA LOGICA
        Parameters
        ----------
        self: [Campana]
            Objeto con propiedades de objeto Campana
        fecha_termino: [date]
            Fecha de termino de la campaña
        Returns
        ----------
        '''
        self.__fecha_termino = fecha_termino
    
    @property
    def anuncios(self) -> List[Anuncio]:
        '''getter de los anuncios
        Parameters
        ----------
        self: [Campana]
            Objeto con propiedades de objeto Campana
        Returns
        ----------
        [List[Anuncio]]
            Retorna el listado de anuncios de la campaña
        '''
        return self.__anuncios

    def __str__(self) -> str:
        '''Sobrecarga del metodo especial __str__ para imprimir los objetos Campana
        Parameters
        ----------
        self: [Campana]
            Objeto con propiedades de objeto Campana
        Returns
        ----------
        '''
        retorno = f"Nombre de la campaña: {self.nombre}\n"
        formatos = (Video, Social, Display)
        cantidad_anuncios = [[sum([1 for anuncio in self.anuncios if isinstance(anuncio, formato)]), formato] for formato in formatos]
        retorno += f"Anuncios: "
        textos_anuncios = []
        for cantidad_anuncio in cantidad_anuncios:
            textos_anuncios.append(f"{cantidad_anuncio[0]} {cantidad_anuncio[1].FORMATO}")
        retorno += ", ".join(textos_anuncios)
        return retorno

anuncios_prueba = [Video(150, "", "", "instream"), Video(150, "", "", "instream"), Social(100, 100, "", "", "facebook")]
prueba = [sum([1 for anuncio in anuncios_prueba if isinstance(anuncio, formato)]) for formato in (Video, Social, Display)]
print(prueba)
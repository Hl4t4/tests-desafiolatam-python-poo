from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str) -> None:
        self.__ancho = self.mayor_a_cero(ancho)
        self.__alto = self.mayor_a_cero(alto)
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
    
    @property
    def ancho(self) -> int:
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho) -> None:
        self.__ancho = self.mayor_a_cero(ancho)

    @property
    def alto(self) -> int:
        return self.__alto
    
    @alto.setter
    def alto(self, alto) -> None:
        self.__alto = self.mayor_a_cero(alto)
    
    @property
    def url_archivo(self) -> str:
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, url_archivo) -> None:
        self.__url_archivo = url_archivo
    
    @property
    def url_clic(self) -> str:
        return self.__url_clic
    
    @url_clic.setter
    def url_clic(self, url_clic) -> None:
        self.__url_clic = url_clic
    
    @property
    def sub_tipo(self) -> str:
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo) -> None:
        if isinstance(self, Video) or isinstance(self, Display) or isinstance(self, Social):
            if sub_tipo in self.SUB_TIPOS:
                self.__sub_tipo = sub_tipo
            else:
                raise SubTipoInvalidoError(self.SUB_TIPOS, sub_tipo)
        else:
            #Posible caso para error de tipo de instancia
            # raise WrongClassError()
            pass
    
    @staticmethod
    def mayor_a_cero(valor:int) -> int:
        if valor > 0:
            return valor
        else:
            return 1
    
    def mostrar_formatos() -> None:
        for formato in (Video, Display, Social):
            print(f"FORMATO {formato.FORMATO}:")
            print("====================")
            for subtipo in formato.SUB_TIPOS:
                print(f"- {subtipo}")
            print('\n')
        

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, duracion: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = self.mayor_a_cero(duracion)
        
    @property
    def duracion(self) -> str:
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion) -> None:
        self.__duracion = self.mayor_a_cero(duracion)
    
    @Anuncio.alto.setter
    def alto(self, alto) -> None:
        pass

    @Anuncio.ancho.setter
    def ancho(self, ancho) -> None:
        pass

    @staticmethod
    def mayor_a_cero(valor:int) -> int:
        if valor > 0:
            return valor
        else:
            return 5
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio(self):
        pass

    def redimensionar_anuncio(self):
        pass

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio(self):
        pass

    def redimensionar_anuncio(self):
        pass

Anuncio.mostrar_formatos()
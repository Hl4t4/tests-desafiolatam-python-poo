from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

#Clase abstracta Anuncio, padre de Video, Display y Social
class Anuncio(ABC):
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str) -> None:
        '''Constructor de la clase Anuncio
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        ancho: [int]
            Ancho del anuncio en pixeles
        alto: [int]
            Alto del anuncio en pixeles
        url_archivo: [str]
            URL al archivo del anuncio
        url_clic: [str]
            URL de hipervinculo del anuncio
        sub_tipo: [str]
            sub tipo segun el tipo de anuncio
        Returns
        ----------
        '''
        self.__ancho = self.mayor_a_cero(ancho)
        self.__alto = self.mayor_a_cero(alto)
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
    
    @property
    def ancho(self) -> int:
        '''getter de atributo ancho
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        Returns
        ----------
        [int]
            Se retorna el ancho del anuncio
        '''
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho:int) -> None:
        '''setter de atributo ancho que comprueba si el valor es mayor a cero
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        ancho: [int]
            URL a modificar del atributo ancho
        Returns
        ----------
        '''
        self.__ancho = self.mayor_a_cero(ancho)

    @property
    def alto(self) -> int:
        '''getter de atributo alto
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        Returns
        ----------
        [int]
            Se retorna el alto del anuncio
        '''
        return self.__alto
    
    @alto.setter
    def alto(self, alto:int) -> None:
        '''setter de atributo alto que comprueba si el valor es mayor a cero
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        alto: [int]
            URL a modificar del atributo alto
        Returns
        ----------
        '''
        self.__alto = self.mayor_a_cero(alto)
    
    @property
    def url_archivo(self) -> str:
        '''getter de atributo url_archivo
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        Returns
        ----------
        [int]
            Se retorna el url del archivo del anuncio
        '''
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, url_archivo:str) -> None:
        '''setter de atributo url_archivo
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        url_archivo: [str]
            URL a modificar del atributo url_archivo
        Returns
        ----------
        '''
        self.__url_archivo = url_archivo
    
    @property
    def url_clic(self) -> str:
        '''getter de atributo url_clic
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        Returns
        ----------
        [int]
            Se retorna el url de clic del anuncio
        '''
        return self.__url_clic
    
    @url_clic.setter
    def url_clic(self, url_clic:str) -> None:
        '''setter de atributo url_clic
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        url_click: [str]
            URL a modificar del atributo url_clic
        Returns
        ----------
        '''
        self.__url_clic = url_clic
    
    @property
    def sub_tipo(self) -> str:
        '''getter de atributo sub_tipo
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        Returns
        ----------
        [int]
            Se retorna el sub tipo del anuncio
        '''
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo:str) -> None:
        '''setter de atributo sub_tipo que comprueba si recibe un valor valido
        Parameters
        ----------
        self: [Anuncio]
            Objeto con propiedades de objeto Anuncio
        sub_tipo: [str]
            Sub tipo a modificar
        Returns
        ----------
        '''
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
        '''Metodo estatico para comprobar si un valor es mayor a cero, sino dar uno por defecto: 1
        Parameters
        ----------
        valor: [int]
            Valor a comprobar
        Returns
        ----------
        [int]
            Se retorna el valor si es mayor a 0, caso contrario se retorna 1
        '''
        if valor > 0:
            return valor
        else:
            return 1
    
    @staticmethod
    def mostrar_formatos() -> None:
        '''Metodo estatico imprimir los formatos y sub tipos validos
        Parameters
        ----------
        Returns
        ----------
        '''
        for formato in (Video, Display, Social):
            print(f"FORMATO {formato.FORMATO}:")
            print("====================")
            for sub_tipo in formato.SUB_TIPOS:
                print(f"- {sub_tipo}")
            print('\n')
        
    @staticmethod
    def formato(sub_tipo:str):
        '''Metodo estatico que comprueba a que formato pertenece un sub tipo, si es que alguno
        Parameters
        ----------
        sub_tipo: [str]
            Sub tipo a utilizar
        Returns
        ----------
        [Video|Display|Social]
            Se retorna la clase a usarse segun sub tipo
        '''
        for formato in (Video, Display, Social):
            if sub_tipo in formato.SUB_TIPOS:
                return formato
        return None

    #Clases abstractas
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

#Clase hija de Video
class Video(Anuncio):
    #Atributos de Clase
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, duracion: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        '''Constructor de la clase Video
        Parameters
        ----------
        self: [Video]
            Objeto con propiedades de objeto Video
        duracion: [int]
            Duracion del video
        url_archivo: [str]
            URL al archivo del video
        url_clic: [str]
            URL de hipervinculo del video
        sub_tipo: [str]
            sub tipo segun el tipo de video
        Returns
        ----------
        '''
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = self.mayor_a_cero(duracion)
        
    @property
    def duracion(self) -> str:
        '''getter de atributo duracion
        Parameters
        ----------
        self: [Video]
            Objeto con propiedades de objeto Video
        Returns
        ----------
        [int]
            Se retorna la duracion del video
        '''
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion:int) -> None:
        '''setter de atributo duracion que comprueba si es mayor a cero
        Parameters
        ----------
        self: [Video]
            Objeto con propiedades de objeto Video
        duracion: [int]
            Tiempo a asignar al video
        Returns
        ----------
        '''
        self.__duracion = self.mayor_a_cero(duracion)
    
    #Sobrecarga del setter de alto para que no se pueda modificar
    @Anuncio.alto.setter
    def alto(self, alto) -> None:
        pass

    #Sobrecarga del setter de ancho para que no se pueda modificar
    @Anuncio.ancho.setter
    def ancho(self, ancho) -> None:
        pass


    @staticmethod
    def mayor_a_cero(valor:int) -> int:
        '''Metodo estatico para comprobar si un valor es mayor a cero, sino dar uno por defecto: 5
        Parameters
        ----------
        valor: [int]
            valor a comprobar
        Returns
        ----------
        [int]
            Se retorna el valor si es mayor a 0, caso contrario se retorna 5
        '''
        if valor > 0:
            return valor
        else:
            return 5
    
    #Metodos no implementados
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    #Atributos de clase
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        '''Constructor de la clase Display
        Parameters
        ----------
        self: [Display]
            Objeto con propiedades de objeto Display
        ancho: [int]
            Ancho del display en pixeles
        alto: [int]
            Alto del display en pixeles
        url_archivo: [str]
            URL al archivo del display
        url_clic: [str]
            URL de hipervinculo del display
        sub_tipo: [str]
            sub tipo segun el tipo de display
        Returns
        ----------
        '''
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    #Atributos de clase
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        '''Constructor de la clase Social
        Parameters
        ----------
        self: [Social]
            Objeto con propiedades de objeto Social
        ancho: [int]
            Ancho del anuncio social en pixeles
        alto: [int]
            Alto del anuncio social en pixeles
        url_archivo: [str]
            URL al archivo del anuncio social
        url_clic: [str]
            URL de hipervinculo del anuncio social
        sub_tipo: [str]
            sub tipo segun el tipo de anuncio social
        Returns
        ----------
        '''
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    #Metodos no implementados
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

#Anuncio.mostrar_formatos()
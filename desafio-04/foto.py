from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        try:
            #Comprobacion si se supera el maximo
            if ancho > Foto.MAX:
                #Se levanta la excepcion por DimensionError
                raise DimensionError("Se ha Producido un error al intentar modificar el ancho", ancho, Foto.MAX)
        except Exception as e:
            #Se imprime el error
            print(e)
        else:
            #asignacion regular
            self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        try:
            #Comprobacion si se supera el maximo
            if alto > Foto.MAX:
                #Se levanta la excepcion por DimensionError
                raise DimensionError("Se ha Producido un error al intentar modificar el alto", alto, Foto.MAX)
        except Exception as e:
            #Se imprime el error
            print(e)
        else:
            #asignacion regular
            self.__alto = alto

#Pruebas
#No se comprueba el error en el constructor
foto = Foto(5000, 500, "swag.png")
#Funciona la excepcion de alto
foto.alto = 5000
#Funciona la excepcion de alto
foto.ancho = 6000
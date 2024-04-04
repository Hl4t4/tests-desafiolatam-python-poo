class Error(Exception):
    """Clase Base Excepciones"""
    pass

class DimensionError(Exception):
    def __init__(self, mensaje:str, dimension:int = None, maximo:int = None) -> None:
        '''Constructor de la clase DimensionError
        Parameters
        ----------
        self: [DimensionError]
            Objeto con propiedades de objeto DimensionError
        dimension: [int]
            Int con la dimension ingresada que causo el error
        maximo: [int]
            Int con la dimension maxima
        Returns
        ----------
        '''
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
    
    def __str__(self) -> str:
        '''Sobrecarga de metodo especial __str__
        Parameters
        ----------
        self: [DimensionError]
            Objeto con propiedades de objeto DimensionError o padre
        Returns
        ----------
        [str]
            Mensaje que se presenta al imprimir la excepcion
        '''
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            if self.dimension is None:
                return f"{self.mensaje}. La dimension maxima es {self.maximo}"
            elif self.maximo is None:
                return f"{self.mensaje}. La dimension ingresada {self.dimension} no es valida"
            return f"{self.mensaje}. La dimension ingresada {self.dimension} es mayor a la maxima {self.maximo}"
class Error(Exception):
    """Clase abstracte base"""
    pass

class LargoExcedidoError(Error):
    def __init__(self, nombre:str, maximo:int, *args: object) -> None:
        '''Constructor de la clase LargoExcedidoError
        Parameters
        ----------
        self: [LargoExcedidoError]
            Objeto con propiedades de objeto LargoExcedidoError
        nombre: [str]
            Nombre ingresado que produjo el error
        maximo: [int]
            Maximo sobrepasado
        args: [object]
            listado de argumentos no definidos en esta instancia
        Returns
        ----------
        '''
        super().__init__(*args)
        self.nombre = nombre
        self.maximo = maximo

class SubTipoInvalidoError(Error):
    def __init__(self, sub_tipos:tuple, sub_tipo:str, *args: object) -> None:
        '''Constructor de la clase SubTipoInvalidoError
        Parameters
        ----------
        self: [SubTipoInvalidoError]
            Objeto con propiedades de objeto SubTipoInvalidoError
        sub_tipos: [tuple]
            Nombres de sub tipos validos
        sub_tipo: [str]
            Sub tipo ingresado que es invalido
        args: [object]
            listado de argumentos no definidos en esta instancia
        Returns
        ----------
        '''
        super().__init__(*args)
        self.sub_tipos = sub_tipos
        self.sub_tipo = sub_tipo

# Para cuando se equivoca de instancia
# class WrongClassError(Error):
#     pass
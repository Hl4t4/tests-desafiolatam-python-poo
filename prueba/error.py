class Error(Exception):
    pass

class LargoExcedidoError(Error):
    def __init__(self, nombre:int, maximo:int, *args: object) -> None:
        super().__init__(*args)
        self.nombre = nombre
        self.maximo = maximo

class SubTipoInvalidoError(Error):
    def __init__(self, sub_tipos:tuple, sub_tipo:str, *args: object) -> None:
        super().__init__(*args)
        self.sub_tipos = sub_tipos
        self.sub_tipo = sub_tipo

# Para cuando se equivoca de instancia
# class WrongClassError(Error):
#     pass
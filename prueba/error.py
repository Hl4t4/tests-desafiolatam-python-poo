class Error(Exception):
    pass

class LargoExcedidoError(Error):
    pass

class SubTipoInvalidoError(Error):
    def __init__(self, subtipos:tuple, subtipo:str, *args: object) -> None:
        super().__init__(*args)
        self.subtipos = subtipos
        self.subtipo = subtipo
    pass

# Para cuando se equivoca de instancia
# class WrongClassError(Error):
#     pass
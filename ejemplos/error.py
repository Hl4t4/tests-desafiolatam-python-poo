class Error(Exception):
    """Clase Base Excepciones"""
    pass

class HoraError(Error):
    pass

class LargoTextoError(Error):
    def __init__(self, mensaje:str, texto:str = None, largo:int = None) -> None:
        self.mensaje = mensaje
        self.texto = (f"{texto[:150]}..." if texto is not None and len(texto) > 150 else texto)
        self.largo = largo

    def __str__(self) -> str:
        if self.texto is None and self.largo is None:
            return super().__str__()
        else:
            ret = f"{self.mensaje}."
            if self.texto != None:
                ret += f" Texto ingresado: {self.texto}."
            if self.largo != None:
                ret += f" Maximo {self.largo} caracteres permitidos."
            return ret
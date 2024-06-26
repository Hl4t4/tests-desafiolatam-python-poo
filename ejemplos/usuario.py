from foto import Foto, FotoPerfil
from typing import Union, List

class Usuario():
    def __init__(self, correo: str, password: str) -> None:
        self.__correo = correo
        self.__password = password
        self.__album_fotos = []
        self.__foto_perfil = FotoPerfil()
    
    @property
    def correo(self) -> str:
        return self.__correo
    
    @correo.setter
    def correo(self, correo: str) -> None:
        self.__correo = correo

    @property
    def password(self) -> str:
        return self.password
    
    @password.setter
    def password(self, password: str) -> None:
        self.__password = password

    @property
    def album_fotos(self) -> List[Foto]:
        return self.__album_fotos
    
    def agregar_fotos_al_album(self, imagen: str, ancho: int, alto: int) -> None:
        self.__album_fotos.append(Foto(imagen, ancho, alto))

    @property
    def foto_perfil(self) -> Foto:
        return self.__foto_perfil
    
    def actualizar_foto_perfil(self, imagen: str, ancho: int, alto: int) -> None:
        self.__foto_perfil.imagen = imagen
        self.__foto_perfil.ancho = ancho
        self.__foto_perfil.alto = alto

    def reaccionar(self, foto: Union[Foto, FotoPerfil]) -> None:
        foto.reacciones += 1
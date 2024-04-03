from abc import ABC, abstractmethod

class tienda(ABC):
    def __init__(self, nombre: str, costo_de_delivery: int):
        pass
    @abstractmethod
    def ingresar_producto(self):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self):
        pass

    @property
    @abstractmethod
    def nombre(self, nombre: str):
        pass
        # self.__nombre = nombre
    
    @property
    @abstractmethod
    def nombre(self, listado_de_productos: list):
        pass
        # self.__listado_de_productos = listado_de_productos

    @property
    @abstractmethod
    def costo_delivery(self, costo_delivery: int):
        pass
        # self.__costo_delivery = costo_delivery


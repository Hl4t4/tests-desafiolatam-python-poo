from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre: str, costo_de_delivery: int):
        pass
    @abstractmethod
    def ingresar_producto(self, nombre:str, precio:int, stock:int):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre:str, cantidad:int):
        pass

    @property
    @abstractmethod
    def nombre(self):
        pass
    
    @property
    @abstractmethod
    def nombre(self):
        pass

    @property
    @abstractmethod
    def costo_delivery(self):
        pass

class Restaurante(Tienda):
    def __init__(self, nombre: str, costo_de_delivery: int):
        self.__nombre = nombre
        self.__costo_de_delivery = costo_de_delivery
        self.__listado_de_productos = [] # ES NECESARIO EN ESTE PUNTO AGREGAR PRODUCTOS O BASTA CON DEJAR EN EL METODO DE ABAJO

    def ingresar_producto(self, nombre:str, precio:int, stock:int = 0):
        nuevo_producto = Producto(nombre, precio)
        if not any(nuevo_producto == producto for producto in self.__listado_de_productos):
            self.__listado_de_productos.append(nuevo_producto)

    def listar_productos(self):
        titulo = (":::::::: LISTADO DE PRODUCTOS :::::::::\n""PRODUCTO\tPRECIO\n")
        listado_de_productos = [f"{producto.nombre}\t\t{producto.precio}\n" for producto in self.__listado_de_productos]
        return f"{titulo}{''.join(listado_de_productos)}"

    def realizar_venta(self, nombre:str, cantidad:int):
        nuevo_producto = Producto(nombre, 0, cantidad)
        comprobacion = [index for index, producto in enumerate(self.__listado_de_productos) if nuevo_producto == producto]
        if comprobacion != []:
            return self.__listado_de_productos[comprobacion[0]].precio * cantidad + self.costo_delivery, cantidad
        else:
            return 0

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def listado_de_productos(self):
        return self.__listado_de_productos

    @property
    def costo_delivery(self):
        return self.__costo_de_delivery
    
class Supermercado(Tienda):
    def __init__(self, nombre: str, costo_de_delivery: int):
        self.__nombre = nombre
        self.__costo_de_delivery = costo_de_delivery
        self.__listado_de_productos = [] # ES NECESARIO EN ESTE PUNTO AGREGAR PRODUCTOS O BASTA CON DEJAR EN EL METODO DE ABAJO

    def ingresar_producto(self, nombre:str, precio:int, stock:int = 0):
        nuevo_producto = Producto(nombre, precio, stock)
        comprobacion = [[index, producto + nuevo_producto] for index, producto in enumerate(self.__listado_de_productos) if nuevo_producto == producto]
        if comprobacion != []:
            self.__listado_de_productos[comprobacion[0][0]] = comprobacion[0][1]
        else:
            self.__listado_de_productos.append(nuevo_producto)

    def listar_productos(self):
        titulo = (":::::::: LISTADO DE PRODUCTOS :::::::::\n""PRODUCTO\tPRECIO\t\tSTOCK\n")
        listado_de_productos = [f"{producto.nombre}\t\t{producto.precio}\t\t{producto.stock} Pocos productos disponibles\n" if producto.stock < 10 else f"{producto.nombre}\t\t{producto.precio}\t\t{producto.stock}\n" for producto in self.__listado_de_productos]
        return f"{titulo}{''.join(listado_de_productos)}"

    def realizar_venta(self, nombre:str, cantidad:int):
        nuevo_producto = Producto(nombre, 0, cantidad)
        comprobacion = [index for index, producto in enumerate(self.__listado_de_productos) if nuevo_producto == producto]
        if comprobacion != []:
            costo = self.__listado_de_productos[comprobacion[0]].precio
            if self.__listado_de_productos[comprobacion[0]] >= nuevo_producto:
                costo = costo * cantidad
                self.__listado_de_productos[comprobacion[0]] = self.__listado_de_productos[comprobacion[0]] - nuevo_producto
            else:
                cantidad = self.__listado_de_productos[comprobacion[0]].stock
                costo = costo * cantidad
                self.__listado_de_productos[comprobacion[0]] = 0
            return (costo + self.costo_delivery), cantidad
        return 0

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def listado_de_productos(self):
        return self.__listado_de_productos

    @property
    def costo_delivery(self):
        return self.__costo_de_delivery
    
class Farmacia(Tienda):
    def __init__(self, nombre: str, costo_de_delivery: int):
        self.__nombre = nombre
        self.__costo_de_delivery = costo_de_delivery
        self.__listado_de_productos = [] # ES NECESARIO EN ESTE PUNTO AGREGAR PRODUCTOS O BASTA CON DEJAR EN EL METODO DE ABAJO

    def ingresar_producto(self, nombre:str, precio:int, stock:int = 0):
        nuevo_producto = Producto(nombre, precio, stock)
        comprobacion = [[index, producto + nuevo_producto] for index, producto in enumerate(self.__listado_de_productos) if nuevo_producto == producto]
        if comprobacion != []:
            self.__listado_de_productos[comprobacion[0][0]] = comprobacion[0][1]
        else:
            self.__listado_de_productos.append(nuevo_producto)

    def listar_productos(self):
        titulo = (":::::::: LISTADO DE PRODUCTOS :::::::::\n""PRODUCTO\tPRECIO\t\tSTOCK\n")
        listado_de_productos = [f"{producto.nombre}\t\t{producto.precio} Envío gratis al solicitar este producto\t\t{producto.stock}\n" if producto.precio > 15000 else f"{producto.nombre}\t\t{producto.precio}\t\t{producto.stock}\n" for producto in self.__listado_de_productos]
        return f"{titulo}{''.join(listado_de_productos)}"

    def realizar_venta(self, nombre:str, cantidad:int):
        nuevo_producto = Producto(nombre, 0, cantidad)
        if cantidad > 3:
            return -1
        comprobacion = [index for index, producto in enumerate(self.__listado_de_productos) if nuevo_producto == producto]
        if comprobacion != []:
            costo = self.__listado_de_productos[comprobacion[0]].precio
            if self.__listado_de_productos[comprobacion[0]] >= nuevo_producto:
                costo = costo * cantidad
                self.__listado_de_productos[comprobacion[0]] = self.__listado_de_productos[comprobacion[0]] - nuevo_producto
            else:
                cantidad = self.__listado_de_productos[comprobacion[0]].stock
                costo = costo * cantidad
                self.__listado_de_productos[comprobacion[0]] = 0
            if self.__listado_de_productos[comprobacion[0]].precio > 10000:
                return costo, cantidad
            else:
                return (costo + self.costo_delivery), cantidad
        return 0

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def listado_de_productos(self):
        return self.__listado_de_productos

    @property
    def costo_delivery(self):
        return self.__costo_de_delivery
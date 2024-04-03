from abc import ABC, abstractmethod
from producto import Producto

#Clase abstracta de tiendas
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
        '''Constructor de la clase Restaurante
        Parameters
        ----------
        self: [Restaurante]
            Objeto Restaurante a generarse
        nombre: [str]
            String con el nombre del Restaurante
        costo_de_delivery: [int]
            Int con el costo de delivery
        Returns
        ----------
        [Restaurante]
            Objeto de tipo  Restaurante con nombre, costo de delivery y listado de productos
        '''
        self.__nombre = nombre
        self.__costo_de_delivery = costo_de_delivery
        self.__listado_de_productos = [] # ES NECESARIO EN ESTE PUNTO AGREGAR PRODUCTOS O BASTA CON DEJAR EN EL METODO DE ABAJO

    def ingresar_producto(self, nombre:str, precio:int, stock:int = 0):
        '''Metodo para ingresar productos
        Parameters
        ----------
        self: [Restaurante]
            Objeto Restaurante a modificar
        nombre: [str]
            String con el nombre del Producto
        precio: [int]
            Int con el precio del Producto
        stock: [int]
            Int con el stock a ingresar, si no se ingresa se asume 0
        Returns
        ----------
        '''
        nuevo_producto = Producto(nombre, precio)
        #Comprobacion si se encuentra entre los productos ya existentes
        if not any(nuevo_producto == producto for producto in self.__listado_de_productos):
            self.__listado_de_productos.append(nuevo_producto)

    def listar_productos(self):
        '''Metodo para presentar los productos del Restaurante
        Parameters
        ----------
        self: [Restaurante]
            Objeto Restaurante a explorar
        Returns
        ----------
        [str]
            String con un titulo de lo que se lista, seguido por lineas de productos con su precio
        '''
        titulo = (":::::::: LISTADO DE PRODUCTOS :::::::::\n""PRODUCTO\tPRECIO\n")
        listado_de_productos = [f"{producto.nombre}\t\t{producto.precio}\n" for producto in self.__listado_de_productos]
        return f"{titulo}{''.join(listado_de_productos)}"

    def realizar_venta(self, nombre:str, cantidad:int):
        '''Metodo para vender los productos del Restaurante
        Parameters
        ----------
        self: [Restaurante]
            Objeto Restaurante a modificar
        nombre: [str]
            String con el nombre del Producto
        cantidad: [int]
            Int con la cantidad de Producto a vender
        Returns
        ----------
        [int] 
            Int con costo 0 porque no se vendio nada
        [tuple]
            Tupla con el valor total de la venta y la cantidad vendida
        '''
        nuevo_producto = Producto(nombre, 0, cantidad)
        #Comprobacion si se encuentra entre los productos ya existentes
        comprobacion = [index for index, producto in enumerate(self.__listado_de_productos) if nuevo_producto == producto]
        if comprobacion != []:
            return self.__listado_de_productos[comprobacion[0]].precio * cantidad + self.costo_delivery, cantidad
        else:
            return 0

    @property
    def nombre(self):
        '''getter de nombre de Restaurante
        Parameters
        ----------
        self: [Restaurante]
            Objeto Restaurante
        Returns
        ----------
        [str]
            Nombre del Restaurante
        '''
        return self.__nombre
    
    @property
    def listado_de_productos(self):
        '''getter del listado de productos de Restaurante
        Parameters
        ----------
        self: [Restaurante]
            Objeto Restaurante
        Returns
        ----------
        [list]
            listado_de_productos del Restaurante
        '''
        return self.__listado_de_productos

    @property
    def costo_delivery(self):
        '''getter de costo de delivery de Restaurante
        Parameters
        ----------
        self: [Restaurante]
            Objeto Restaurante
        Returns
        ----------
        [int]
            Nombre del Restaurante
        '''
        return self.__costo_de_delivery
    
class Supermercado(Tienda):
    def __init__(self, nombre: str, costo_de_delivery: int):
        '''Constructor de la clase Supermercado
        Parameters
        ----------
        self: [Supermercado]
            Objeto Supermercado a generarse
        nombre: [str]
            String con el nombre del Supermercado
        costo_de_delivery: [int]
            Int con el costo de delivery
        Returns
        ----------
        [Supermercado]
            Objeto de tipo  Supermercado con nombre, costo de delivery y listado de productos
        '''
        self.__nombre = nombre
        self.__costo_de_delivery = costo_de_delivery
        self.__listado_de_productos = [] # ES NECESARIO EN ESTE PUNTO AGREGAR PRODUCTOS O BASTA CON DEJAR EN EL METODO DE ABAJO

    def ingresar_producto(self, nombre:str, precio:int, stock:int = 0):
        '''Metodo para ingresar productos
        Parameters
        ----------
        self: [Supermercado]
            Objeto Supermercado a modificar
        nombre: [str]
            String con el nombre del Producto
        precio: [int]
            Int con el precio del Producto
        stock: [int]
            Int con el stock a ingresar, si no se ingresa se asume 0
        Returns
        ----------
        '''
        nuevo_producto = Producto(nombre, precio, stock)
        #Comprobacion si se encuentra entre los productos ya existentes
        comprobacion = [[index, producto + nuevo_producto] for index, producto in enumerate(self.__listado_de_productos) if nuevo_producto == producto]
        if comprobacion != []:
            #En caso de que ya exista, se guarda la suma de los stock
            self.__listado_de_productos[comprobacion[0][0]] = comprobacion[0][1]
        else:
            self.__listado_de_productos.append(nuevo_producto)

    def listar_productos(self):
        '''Metodo para presentar los productos del Supermercado
        Parameters
        ----------
        self: [Supermercado]
            Objeto Supermercado a explorar
        Returns
        ----------
        [str]
            String con un titulo de lo que se lista, seguido por lineas de productos con su precio y stock, con avisos si quedan pocos
        '''
        titulo = (":::::::: LISTADO DE PRODUCTOS :::::::::\n""PRODUCTO\tPRECIO\t\tSTOCK\n")
        listado_de_productos = [f"{producto.nombre}\t\t{producto.precio}\t\t{producto.stock} Pocos productos disponibles\n" if producto.stock < 10 else f"{producto.nombre}\t\t{producto.precio}\t\t{producto.stock}\n" for producto in self.__listado_de_productos]
        return f"{titulo}{''.join(listado_de_productos)}"

    def realizar_venta(self, nombre:str, cantidad:int):
        '''Metodo para vender un producto del Supermercado
        Parameters
        ----------
        self: [Supermercado]
            Objeto Supermercado a modificar
        nombre: [str]
            String con el nombre del Producto
        cantidad: [int]
            Int con la cantidad de Producto a vender
        Returns
        ----------
        [int] 
            Int con costo 0 porque no se vendio nada
        [tuple]
            Tupla con el valor total de la venta y la cantidad vendida
        '''
        nuevo_producto = Producto(nombre, 0, cantidad)
        #Comprobacion si se encuentra entre los productos ya existentes
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
        '''getter de nombre de Supermercado
        Parameters
        ----------
        self: [Supermercado]
            Objeto Supermercado
        Returns
        ----------
        [str]
            Nombre del Supermercado
        '''
        return self.__nombre
    
    @property
    def listado_de_productos(self):
        '''getter del listado de productos de Supermercado
        Parameters
        ----------
        self: [Supermercado]
            Objeto Supermercado
        Returns
        ----------
        [list]
            listado_de_productos del Supermercado
        '''
        return self.__listado_de_productos

    @property
    def costo_delivery(self):
        '''getter de costo de delivery de Supermercado
        Parameters
        ----------
        self: [Supermercado]
            Objeto Supermercado
        Returns
        ----------
        [int]
            Nombre del Supermercado
        '''
        return self.__costo_de_delivery
    
class Farmacia(Tienda):
    def __init__(self, nombre: str, costo_de_delivery: int):
        '''Constructor de la clase Farmacia
        Parameters
        ----------
        self: [Farmacia]
            Objeto Farmacia a generarse
        nombre: [str]
            String con el nombre de la Farmacia
        costo_de_delivery: [int]
            Int con el costo de delivery
        Returns
        ----------
        [Farmacia]
            Objeto de tipo Farmacia con nombre, costo de delivery y listado de productos
        '''
        self.__nombre = nombre
        self.__costo_de_delivery = costo_de_delivery
        self.__listado_de_productos = [] # ES NECESARIO EN ESTE PUNTO AGREGAR PRODUCTOS O BASTA CON DEJAR EN EL METODO DE ABAJO

    def ingresar_producto(self, nombre:str, precio:int, stock:int = 0):
        '''Metodo para ingresar productos
        Parameters
        ----------
        self: [Farmacia]
            Objeto Farmacia a modificar
        nombre: [str]
            String con el nombre del Producto
        precio: [int]
            Int con el precio del Producto
        stock: [int]
            Int con el stock a ingresar, si no se ingresa se asume 0
        Returns
        ----------
        '''
        nuevo_producto = Producto(nombre, precio, stock)
        #Comprobacion si se encuentra entre los productos ya existentes
        comprobacion = [[index, producto + nuevo_producto] for index, producto in enumerate(self.__listado_de_productos) if nuevo_producto == producto]
        if comprobacion != []:
            #En caso de que ya exista, se guarda la suma de los stock
            self.__listado_de_productos[comprobacion[0][0]] = comprobacion[0][1]
        else:
            self.__listado_de_productos.append(nuevo_producto)

    def listar_productos(self):
        '''Metodo para presentar los productos de la Farmacia
        Parameters
        ----------
        self: [Farmacia]
            Objeto Farmacia a explorar
        Returns
        ----------
        [str]
            String con un titulo de lo que se lista, seguido por lineas de productos con su precio y stock, con avisos de envios gratuito
        '''
        titulo = (":::::::: LISTADO DE PRODUCTOS :::::::::\n""PRODUCTO\tPRECIO\t\tSTOCK\n")
        listado_de_productos = [f"{producto.nombre}\t\t{producto.precio} Envío gratis al solicitar este producto\t\t{producto.stock}\n" if producto.precio > 15000 else f"{producto.nombre}\t\t{producto.precio}\t\t{producto.stock}\n" for producto in self.__listado_de_productos]
        return f"{titulo}{''.join(listado_de_productos)}"

    def realizar_venta(self, nombre:str, cantidad:int):
        '''Metodo para vender un producto de la Farmacia
        Parameters
        ----------
        self: [Farmacia]
            Objeto Farmacia a modificar
        nombre: [str]
            String con el nombre del Producto
        cantidad: [int]
            Int con la cantidad de Producto a vender
        Returns
        ----------
        [int] 
            Int con costo 0 porque no se vendio nada, -1 si intentan vender mas de 3 productos
        [tuple]
            Tupla con el valor total de la venta y la cantidad vendida
        '''
        nuevo_producto = Producto(nombre, 0, cantidad)
        #Caso de mas de 3 productos pedidos de una no hace cambios
        if cantidad > 3:
            return -1
        #Comprobacion si se encuentra entre los productos ya existentes
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
            #No se aplica costo de envio para precio de producto individual mayor a 10000
            if self.__listado_de_productos[comprobacion[0]].precio > 10000:
                return costo, cantidad
            else:
                return (costo + self.costo_delivery), cantidad
        return 0

    @property
    def nombre(self):
        '''getter del listado de productos de Farmacia
        Parameters
        ----------
        self: [Farmacia]
            Objeto Farmacia
        Returns
        ----------
        [list]
            listado_de_productos de la Farmacia
        '''
        return self.__nombre
    
    @property
    def listado_de_productos(self):
        '''getter del listado de productos de Farmacia
        Parameters
        ----------
        self: [Farmacia]
            Objeto Farmacia
        Returns
        ----------
        [list]
            listado_de_productos de la Farmacia
        '''
        return self.__listado_de_productos

    @property
    def costo_delivery(self):
        '''getter de costo de delivery de laFarmacia
        Parameters
        ----------
        self: [Farmacia]
            Objeto Farmacia
        Returns
        ----------
        [int]
            Nombre de la Farmacia
        '''
        return self.__costo_de_delivery
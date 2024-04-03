class Producto():
    def __init__(self, nombre:str, precio:int, stock:int = 0):
        '''Constructor de la clase Producto
        Parameters
        ----------
        self: [Producto]
            Objeto Producto a generarse
        nombre: [str]
            String con el nombre del producto
        precio: [int]
            Int con el precio individual del producto
        stock: [int]
            Int con el stock inicial del producto, en caso de no explicitarse se asume 0
        Returns
        ----------
        [Producto]
            Objeto de tipo  producto con nombre, precio y stock
        '''
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        '''getter de nombre de Producto
        Parameters
        ----------
        self: [Producto]
            Objeto Producto
        Returns
        ----------
        [str]
            Nombre del Producto
        '''
        return self.__nombre
    
    @property
    def precio(self):
        '''getter de precio de Producto
        Parameters
        ----------
        self: [Producto]
            Objeto Producto
        Returns
        ----------
        [str]
            Precio del Producto
        '''
        return self.__precio
    
    @property
    def stock(self):
        '''getter del stock de Producto
        Parameters
        ----------
        self: [Producto]
            Objeto Producto
        Returns
        ----------
        [str]
            Stock del Producto
        '''
        return self.__stock
    
    @stock.setter
    def stock(self, stock:int):
        '''setter del stock de Producto que en caso de ser menor a 0 se iguala a 0
        Parameters
        ----------
        self: [Producto]
            Objeto Producto
        Returns
        ----------
        '''
        if stock < 0:
            self.__stock = 0
        else:
            self.__stock = stock

    def __add__(self, other):
        '''Sobrecarga de la funcion suma
        Parameters
        ----------
        self: [Producto]
            Objeto Producto
        other: [Producto]
            otro Objeto Producto
        Returns
        ----------
        [Producto]
            Objeto Producto con los stock sumados
        '''
        self.stock = self.stock + other.stock
        return self
    
    def __sub__(self, other):
        '''Sobrecarga de la funcion resta
        Parameters
        ----------
        self: [Producto]
            Objeto Producto
        other: [Producto]
            otro Objeto Producto
        Returns
        ----------
        [Producto]
            Objeto Producto con los stock restados
        '''
        self.stock = self.stock - other.stock
        return self
    
    def __eq__(self, other):
        '''Sobrecarga de equivalente
        Parameters
        ----------
        self: [Producto]
            Objeto Producto
        other: [Producto]
            otro Objeto Producto
        Returns
        ----------
        [bool]
            Booleano de la equivalencia de nombre de dos Productos
        '''
        return self.nombre == other.nombre
    
    def __ge__(self, other):
        '''Sobrecarga de la funcion greater than
        Parameters
        ----------
        self: [Producto]
            Objeto Producto
        other: [Producto]
            otro Objeto Producto
        Returns
        ----------
        [bool]
            Booleano de la comparacion mayor o igual del stock de dos Productos
        '''
        return self.stock >= other.stock
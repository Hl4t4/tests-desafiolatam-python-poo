class Producto():
    def __init__(self, nombre:str, precio:int, stock:int = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, stock:int):
        if stock < 0:
            self.stock = 0
        else:
            self.stock = stock

    def __add__(self, other):
        self.stock = self.stock + other.stock
        return self
    
    def __sub__(self, other):
        self.stock = self.stock - other.stock
        return self
    
    def __eq__(self, other):
        return self.nombre == other.nombre
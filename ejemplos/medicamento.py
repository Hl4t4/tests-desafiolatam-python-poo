# archivo medicamento.py
class Medicamento():
    IVA = 0.18
    def __init__(self, nombre : str, stock: int = 0):
        self.descuento = 0.0
        self.precio_bruto = 0
        self.precio_final = 0.0
        self.nombre = nombre
        self.stock = stock

    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()
    
    def __iadd__(self, other):
        if self == other:
            self.stock += other.stock
        return self

    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0

    @property
    def precio(self):
        return self.precio_final
    
    @precio.setter
    def precio(self, precio_bruto: int):
        if self.validar_mayor_a_cero(precio_bruto):
            self.precio_bruto = precio_bruto
            precio_final = precio_bruto * (1+self.IVA)
            if precio_final >= 10000 and self.precio < 20000:
                self.descuento = 0.1
            elif precio_final >= 20000 and self.precio < 30000:
                self.descuento = 0.2
            self.precio_final = precio_final * (1-self.descuento)

    
    def asigna_precio(self, precio_entregado: int):
        es_valido = self.validar_mayor_a_cero(precio_entregado)
        if es_valido:
            self.precio = precio_entregado
            self.descuento = 0.0

            if self.precio >= 10000 and self.precio < 20000:
                self.descuento = 0.1
            elif self.precio >= 20000 and self.precio < 30000:
                self.descuento = 0.2
            elif self.precio >= 30000:
                self.descuento = 0.3
        else:
            print(f"El precio '{precio_entregado}' no es un precio valido")
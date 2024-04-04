import json
instancias = []

class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio

with open("productos.txt") as productos:
    linea = productos.readline()
    while linea:
        producto = json.loads(linea)
        instancias.append(Producto(producto.get("nombre"), producto.get("precio")))
        linea = productos.readline()

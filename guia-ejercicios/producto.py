import json
from datetime import datetime
instancias = []

class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio

with open("productos.txt") as productos:
    linea = productos.readline()
    while linea:
        try:
            producto = json.loads(linea)
            instancias.append(Producto(producto.get("nombre"), producto.get("precio")))
        except Exception as e:
            with open("error.log", "a+") as log:
                now = datetime.now()
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e.__str__()}\n")
        finally:
            linea = productos.readline()
        

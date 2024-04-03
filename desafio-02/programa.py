from tienda import Restaurante, Supermercado, Farmacia

def creacion_tienda():
    '''Funcion que pide al usuario los datos para crear una tienda
    Parameters
    ----------
    Returns
    ----------
    [Restaurante, Supermercado, Farmacia]
        Objeto tienda especifico a un tipo con nombre y costo de delivery
    '''
    print("Que tipo de tienda desea crear")
    print("1. Restaurante")
    print("2. Supermercado")
    print("3. Farmacia")
    tipo = int(input())
    nombre = input("\nNombre de la tienda: ")
    costo_de_delivery = int(input("Costo del delivery: "))
    tienda = None
    if tipo == 1:
        tienda = Restaurante(nombre, costo_de_delivery)
    elif tipo == 2:
        tienda = Supermercado(nombre, costo_de_delivery)
    elif tipo == 3:
        tienda = Farmacia(nombre, costo_de_delivery)
    return tienda

def ingresar_productos(tienda):
    '''Funcion que pide al usuario que ingrese productos
    Parameters
    ----------
    tienda: [Restaurante / Supermercado / Farmacia]
        Objeto tienda de un tipo especifico
    Returns
    ----------
    [Restaurante / Supermercado / Farmacia]
        Objeto tienda de un tipo especifico con los productos agregados
    '''
    print("\nPor favor ingrese los productos de la tienda")
    opcion = "y"
    while opcion == "y":
        print("Para ingresar un producto debe agregar")
        nombre = input("Nombre: ")
        precio = int(input("Precio: "))
        stock = 0
        if (type(tienda) != Restaurante):
            stock = int(input("Stock: "))
        tienda.ingresar_producto(nombre, precio, stock)
        opcion = input("Desea continuar agregando productos? \"y\"/\"n\"\n")
    return tienda

def elecciones(tienda):
    '''Funcion que pide el usuario elegir entre listar productos, realizar ventas o salir del programa
    Parameters
    ----------
    tienda: [Restaurante / Supermercado / Farmacia]
        Objeto tienda de un tipo especifico
    Returns
    ----------
    [Restaurante / Supermercado / Farmacia]
        Objeto tienda de un tipo especifico con productos descontados de ventas realizadas
    '''
    opcion = None
    while opcion != 3:
        print("\nQue accion desea realizar")
        print("1. Listar productos existentes")
        print("2. Realizar una venta")
        print("3. Salir del programa")
        opcion = int(input())

        if opcion == 1:
            print(tienda.listar_productos())
        elif opcion == 2:
            print("\nQue producto desea vender?")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            venta = tienda.realizar_venta(nombre, cantidad)
            if venta == 0:
                print("El producto no se encuentra disponible")
            elif venta == -1:
                print("Solo se permite vender hasta 3 del mismo producto al mismo tiempo")
            else:
                costo, cantidad = venta
                print(f"El costo total es de {costo}, por una cantidad de {cantidad} del producto {nombre}")
    return tienda

#Carga principal
tienda = creacion_tienda()
if tienda != None:
    tienda = ingresar_productos(tienda)
    tienda = elecciones(tienda)
    
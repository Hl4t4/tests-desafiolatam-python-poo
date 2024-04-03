from medicamento import Medicamento

# precio = int(input("Ingrese un precio a validar:\n"))
# es_valido = Medicamento.validar_mayor_a_cero(precio)

# if es_valido:
#     print("El precio ingresado es válido")
# else:
#     print("El precio ingresado no es válido")

# m1 = Medicamento()
# m2 = Medicamento()

# if m1.IVA == m2.IVA and m1.descuento == m2.descuento:
#     print("Todas las instancias tienen igual descuento e IVA")
#     print("El valor del IVA es: ", Medicamento.IVA)
#     print("El valor del descuento es:", Medicamento.descuento)

# nombre = input("Ingrese nombre del medicamento:\n")
# stock = int(input("Ingrese stock del medicamento:\n"))
# precio_bruto = int(input("Ingrese precio bruto del medicamento:\n"))

# m1 = Medicamento(nombre, stock)
# m1.precio = precio_bruto

# print(f"El precio bruto del medicamento {m1.nombre} es {m1.precio_bruto}")
# if m1.descuento:
#     print(f"Tiene un descuento de {m1.descuento * 100}%")

# print(f"El precio final del medicamento es {m1.precio_final}")

opcion_ingreso = int(input("¿Desea agregar un medicamento?"
"\n1. Sí\n2. No\n"))
ingresados = []

while opcion_ingreso == 1:
    nombre = input("\nIngrese nombre del medicamento:\n")
    stock = int(input("\nIngrese stock del medicamento:\n"))
    m = Medicamento(nombre, stock)
    if m in ingresados:
        indice = ingresados.index(m)
        ingresados[indice] += m
    else:
        ingresados.append(m)
        precio_bruto = int(input("\nIngrese precio bruto del medicamento:\n"))
        m.precio = precio_bruto
    print(f"\n***** DATOS MEDICAMENT1O {m.nombre} *****")
    print(f"PRECIO BRUTO: ${m.precio_bruto}")
    if m.descuento:
        print(f"DESCUENTO: {m.descuento*100}%")
    print(f"PRECIO FINAL: ${m.precio_final}")
    print(f"STOCK: {m.stock}")
    print(f"\nLa farmacia cuenta con {len(ingresados)} medicamento(s)\n")
    opcion_ingreso = int(input("¿Desea agregar un medicamento? \n1. Sí\n2. No\n"))
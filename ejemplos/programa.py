from medicamento import Medicamento

precio = int(input("Ingrese un precio a validar:\n"))
es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido:
    print("El precio ingresado es válido")
else:
    print("El precio ingresado no es válido")

m1 = Medicamento()
m2 = Medicamento()

if m1.IVA == m2.IVA and m1.descuento == m2.descuento:
    print("Todas las instancias tienen igual descuento e IVA")
    print("El valor del IVA es: ", Medicamento.IVA)
    print("El valor del descuento es:", Medicamento.descuento)
from medicamento import Medicamento

medicamento_nuevo = Medicamento()

precio = int(input("Ingrese precio del medicamento\n"))
medicamento_nuevo.asigna_precio(precio)

print(medicamento_nuevo.precio)
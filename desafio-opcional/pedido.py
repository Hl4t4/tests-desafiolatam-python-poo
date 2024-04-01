from te import Te

def tipos_de_te():
    print("Tiene para elegir entre:")
    print("Te Negro")
    print("Te Verde")
    print("Agua de hierbas")
    entrada =  input().lower()
    if entrada == "te negro":
        return 1, "Te Negro"
    elif entrada == "te verde":
        return 2, "Te Verde"
    elif entrada == "agua de hierbas":
        return 3, "Agua de Hierbas"
    else:
        return tipos_de_te()

def tipos_de_formato():
    print("Tiene para elegir entre:")
    print("300 [gr]")
    print("500 [gr]")
    return int(input())
    
numero_de_te, tipo_de_te = tipos_de_te()
tipo_de_formato = tipos_de_formato()

tiempo, recomendacion = Te.tiempo_y_recomendacion(numero_de_te)
precio = Te.precio(tipo_de_formato)

print (f'Sabor del tipo de te: {tipo_de_te}')
print (f'Formato: {tipo_de_formato} [gr]')
print (f'Precio: ${precio}')
print (f'Tiempo: {tiempo}')
print (f'Recomendacion: {recomendacion}')
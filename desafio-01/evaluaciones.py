from pizza import Pizza

def print_atributes():
    '''Funcion para imprimir atributos de la clase Pizza no iniciada
    '''
    print(f"El precio es: {Pizza.precio}")
    print(f"El tamaño es: {Pizza.size}")
    print(f"Los ingredientes proteicos son: {Pizza.proteicos}")
    print(f"Los ingredientes vegetales son: {Pizza.vegetales}")

def print_atributes_iniciado(nueva_pizza: Pizza):
    '''Funcion para imprimir atributos de un objeto Pizza
    '''
    print(f"El precio es: {nueva_pizza.precio}")
    print(f"El tamaño es: {nueva_pizza.size}")
    print(f"Los ingredientes proteicos son: {nueva_pizza.proteicos}")
    print(f"Los ingredientes vegetales son: {nueva_pizza.vegetales}")
    print(f"El tipo de masa es: {nueva_pizza.masa}")
    if nueva_pizza.valida:
        print("Es una pizza valida")
    else:
        print("No es una pizza valida")

elemento_a_probar = "salsa de tomate"
listado_ingredientes = ["salsa de tomate", "salsa bbq"]

#Punto 5.a
print_atributes()

#Punto 5.b
print(Pizza.validar_de_lista(elemento_a_probar, listado_ingredientes))

#Punto 5.c
nueva_pizza = Pizza()
nueva_pizza.realizar_pedido()

#Punto 5.d
print_atributes_iniciado(nueva_pizza)

#Punto 5.e
print(Pizza.valida)
from personaje import Personaje

nombre = input("Bienvenido a RPG The Game \nIngrese el nombre de su personaje por favor:\n")

#Creacion de personajes
personaje1 = Personaje(nombre)
personaje1_nombre, personaje1_nivel, personaje1_experiencia = personaje1.estado

orco = Personaje("Orco")
orco_nombre, orco_nivel, orco_experiencia = orco.estado

accion = 1

print(f'NOMBRE: {personaje1_nombre}\t NIVEL:{personaje1_nivel}\t EXP:{personaje1_experiencia}')
while(accion == 1):
    #Calculo de la probabilidad de ganar
    probabilidad = personaje1.instancia(personaje1, orco)
    #Impresion de pantalla de informacion y solicitud de accion
    accion = personaje1.opciones_y_accion(probabilidad, orco_nombre)
    #Resultado del combate
    combate = personaje1.resultado(personaje1, orco, accion, probabilidad)

    #Cambios de estado
    if combate == 1: 
        personaje1.estado = 50
        orco.estado = -30
    elif combate == -1:
        personaje1.estado = -30
        orco.estado = 50

    personaje1_nombre, personaje1_nivel, personaje1_experiencia = personaje1.estado
    orco_nombre, orco_nivel, orco_experiencia = orco.estado

    #Presentacion de cambios de estado
    print(f'\nNOMBRE: {personaje1_nombre}\t NIVEL:{personaje1_nivel}\t EXP:{personaje1_experiencia}')
    print(f'NOMBRE: {orco_nombre}\t NIVEL:{orco_nivel}\t EXP:{orco_experiencia}\n')




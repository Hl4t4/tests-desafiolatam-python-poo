from personaje import Monstruo, Jugador

begimo = Monstruo(1000, 1, 8)
jugador = Jugador(500, 10, 5, "espada")


# while(jugador.hp > 0):
#     print("Procedes a atacar a Begimo!\n")
#     ataque_jugador = jugador.atacar()
#     begimo.defender(ataque_jugador)
#     if begimo.hp > 0:
#         print("Begimo vive y te ataca!\n")
#         ataque_begimo = begimo.atacar()
#         jugador.defender(ataque_begimo)
#     else:
#         print("Felicidades jugador has Ganado")
#         print(f"Tu vida restante es {jugador.hp} HP")
#         break
# else:
#     print("Oh no! Begimo ha logrado derrotarte!")
#     print(f"Lo ha logrado con un total de vida de {begimo.hp} HP")

enfrentados = [Jugador(500, 10, 5, "espada"), Monstruo(1000, 1, 8)]
atk = 0

while any(e.hp <= 0 for e in enfrentados) == False:
    for e in enfrentados:
        if atk:
            e.defender(atk)
        if e.hp > 0:
            atk = e.atacar()
        else:
            print(f"¡Oh no!, el {e.__class__.__name__} ha muerto :(")
            break
        
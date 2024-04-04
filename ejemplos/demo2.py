from personaje2 import Monstruo, Jugador

monstruo = Monstruo(HP = 1000, ATK = 1, DF = 8, nombre = "Begimo")
monstruo.mostrar_dialogo("GRAAAWR")

enfrentados = [Jugador(500, 10, 5, "espada"), monstruo]
atk = 0

while any(e.hp <= 0 for e in enfrentados) == False:
    for e in enfrentados:
        if atk:
            e.defender(atk)
        if e.hp > 0:
            atk = e.atacar()
        else:
            if isinstance(e, Monstruo):
                print("¡Felicidades!, ¡Haz ganado la batalla!")
            elif isinstance(e, Jugador):
                print("¡Oh no!, haz perdido la batalla :(")
            break
        
from error import HoraError, LargoTextoError
from reunion import Reunion
import re

titulo = None
hora = None
time_re = "^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$"

while True:
    try:
        if titulo is None or len(titulo) > 150:
            titulo = input("\nIngrese titulo de la reunion"" (Maximo 150 caracteres):\n")

            if len(titulo) > 150:
                raise LargoTextoError("Titulo de la reunion excede maximo de caracteres", titulo, 150)
            
        if hora is None or re.search(time_re, hora) is None:
            hora = input("\nIngrese hora de la reunión"" (Formato: HH:MM:SS):\n")

            if re.search(time_re, hora) is None:
                raise HoraError("Formato de Hora debe ser HH:MM:SS.")
    except Exception as e:
        print(f"\n{e}\n")
        continue
    else:
        break
r = Reunion(titulo, hora)
print("\nReunion creada correctamente.")
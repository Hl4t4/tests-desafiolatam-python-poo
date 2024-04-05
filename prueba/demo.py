from campana import Campana
from datetime import datetime
from error import SubTipoInvalidoError, LargoExcedidoError

anuncio_dict = {"duracion" : 50, "url_archivo" : "direccion.com", "url_clic" : "direccion.cl", "sub_tipo" : "instream"}
super_campana = Campana(nombre="Super Campana", fecha_inicio=datetime.now(), fecha_termino=datetime.now(), anuncio= anuncio_dict)

print(super_campana)

try:
    sub_tipo = input("Introduzca el nuevo sub tipo para el anuncio\n\n")
    super_campana.anuncios[0].sub_tipo = sub_tipo
except SubTipoInvalidoError as e:
    with open("error.log", "a+") as log:
        log.write(f"El sub tipo {e.sub_tipo} no es un valor valido para este tipo de anuncio, solo pueden ser {e.sub_tipos}")
        log.close()
except Exception as e:
    with open("error.log", "a+") as log:
        log.write(e.__str__())
        log.close()
try:
    nombre = input("Introduzca el nuevo nombre de la campaña\n\n")
    super_campana.nombre = nombre
except LargoExcedidoError as e:
    with open("error.log", "a+") as log:
        log.write(f"El sub tipo {e.nombre} no es un valor valido para el nombre de campaña, el maximo de caracteres es {e.maximo}")
        log.close()
except Exception as e:
    with open("error.log", "a+") as log:
        log.write(e.__str__())
        log.close()

print(super_campana)
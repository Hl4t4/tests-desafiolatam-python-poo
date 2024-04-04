from usuario import Usuario
import json
import os

usuarios = []

try:
    archivo_usuarios = open(os.path.abspath("usuarios.txt"), "r")
    linea = archivo_usuarios.readline()
    while linea:
        usuario = json.loads(linea)
        #No hay error en caso de que falte uno de los properties debido a que None es un valor aceptado por la clase
        usuarios.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
        linea = archivo_usuarios.readline()
except FileNotFoundError as e:
    #Caso que no se encuentra el archivo para leer
    with open(os.path.abspath("logs/error.log"), "a") as log:
        log.seek(0)
        log.write(e.__str__()+"\n")
        log.close()
except OSError as e:
    #Errores de open
    with open(os.path.abspath("logs/error.log"), "a") as log:
        log.seek(0)
        log.write(e.__str__()+"\n")
        log.close()
except NameError as e:
    # Error al cargar una variable que no existe
    with open(os.path.abspath("logs/error.log"), "a") as log:
        log.seek(0)
        log.write(e.__str__()+"\n")
        log.close()
except json.decoder.JSONDecodeError as e:
    #Errores al decodificar el json
    with open(os.path.abspath("logs/error.log"), "a") as log:
        log.seek(0)
        match e.msg:
            # Error al no tener un valor entre comillas despues de un property name y sus :
            case "Expecting value":
                log.write(f"Error en la linea {e.doc.strip()} El tipo de error es {e.msg} en el caracter {e.colno}\n")
            # Error que no encuentra un delimitador entre properties
            case "Expecting ',' delimiter":
                log.write(f"Error en la linea {e.doc.strip()} El tipo de error es {e.msg}\n")
            # Error que no encuentra : despues de la identificacion de un property name
            case "Expecting ':' delimiter":
                log.write(f"Error en la linea {e.doc.strip()} El tipo de error es {e.msg}\n")
            # No encuentra el nombre de la property
            case "Expecting property name enclosed in double quotes":
                log.write(f"Error en la linea {e.doc.strip()} El tipo de error es {e.msg} error en la property en el caracter {e.colno}\n")
            # Error cuando encuentra datos que no conformas con un JSON en particular se probo una linea que no parte con {
            case "Extra data":
                log.write(f"Error en la linea {e.doc.strip()} El tipo de error es {e.msg} datos que no son un json\n")
            case _:
            # Errores no atajados por los anteriores
                log.write(f"Error en la linea {e.doc.strip()} El tipo de error es {e.msg}\n")
        log.close()
else:
    archivo_usuarios.close()
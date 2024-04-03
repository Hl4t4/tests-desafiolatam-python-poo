import random

class Personaje():
    def __init__ (self, nombre:str):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        return self.nombre, self.nivel, self.experiencia
    
    @estado.setter
    def estado(self, experiencia:int):
        experiencia_temporal = self.experiencia + experiencia
        if experiencia < 0:
            if experiencia_temporal < 0:
                niveles_a_bajar = experiencia_temporal // 100
                self.nivel = self.nivel + niveles_a_bajar
                if self.nivel < 1:
                    self.nivel = 1
                    self.experiencia = 0
                else:
                    self.experiencia = 100 - (experiencia_temporal % 100)
            else:
                self.experiencia = experiencia_temporal
        else:
            niveles_a_subir = experiencia_temporal // 100
            self.nivel = self.nivel + niveles_a_subir
            self.experiencia = experiencia_temporal % 100

    def __gt__ (self, other):
        return self.nivel > other.nivel
    
    def __lt__ (self, other):
        return self.nivel < other.nivel
    
    def __eq__ (self, other):
        return self.nivel == other.nivel
    
    @staticmethod
    def instancia(self, other):
        if self > other:
            return 0.66
        elif self < other:
            return 0.33
        else:
            return 0.50
        
    @staticmethod
    def opciones_y_accion(probabilidad: float, oponente: str):
        print(f"Oh no! Ha aparecido un {oponente}")
        print(f"Con tu nivel actual, tienes {probabilidad*100}% de probabilidades de ganarle al {oponente}\n")

        print(f"En caso de ganarle, recibiras 50 puntos de experiencia y el {oponente} perdera 30")
        print(f"En caso de perder, perderas 30 puntos de experiencia y el {oponente} ganara 50\n")

        print("Deseas")
        print("1. Atacar")
        print("2. Huir")
        return int(input())
    
    @staticmethod
    def resultado(self, other, accion: int, probabilidad: float):
        if accion == 2:
            print("El orco ha quedado atras")
            return 0
        elif accion == 1:
            combate = probabilidad - random.uniform(0.0, 1.0)
            if combate >= 0:
                print(f"Ganaste contra tu {other.nombre}")
                return 1
            else:
                print(f"Perdiste contra tu {other.nombre}")
                return -1


import random

class Personaje():
    def __init__ (self, nombre:str):
        '''Constructor de Personaje
        Parameters
        ----------
        self: [Personaje]
            Objeto personaje a generarse
        nombre: [str]
            El nombre del personaje
        '''
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        '''Getter de estado del personaje
        Parameters
        ----------
        self: [Personaje]
            Objeto personaje que se quiere obtener datos
        Returns
        ----------
        [tuple]
            Nombre, nivel y experiencia del personaje
        '''
        return self.nombre, self.nivel, self.experiencia
    
    @estado.setter
    def estado(self, experiencia:int):
        '''Setter del estado del personaje, sube o baja el nivel segun experiencia recibida
        Parameters
        ----------
        self: [Personaje]
            Objeto personaje que se quiere modificar datos
        experiencia: [int]
            Experiencia a ganar o perder
        '''
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
        '''Sobrecarga de greater than
        Parameters
        ----------
        self: [Personaje]
            Objeto personaje que se quiere comparar
        other: [Personaje]
            Objeto personaje que se quiere comparar
        Returns
        ----------
        [bool]
            El resultado de si el primer Personaje tiene mayor nivel que el segundo
        '''
        return self.nivel > other.nivel
    
    def __lt__ (self, other):
        '''Sobrecarga de less than
        Parameters
        ----------
        self: [Personaje]
            Objeto personaje que se quiere comparar
        other: [Personaje]
            Objeto personaje que se quiere comparar
        Returns
        ----------
        [bool]
            El resultado de si el primer Personaje tiene menor nivel que el segundo
        '''
        return self.nivel < other.nivel
    
    def __eq__ (self, other):
        '''Sobrecarga de equal
        Parameters
        ----------
        self: [Personaje]
            Objeto personaje que se quiere comparar
        other: [Personaje]
            Objeto personaje que se quiere comparar
        Returns
        ----------
        [bool]
            El resultado de si el primer Personaje tiene el mismo nivel que el segundo
        '''
        return self.nivel == other.nivel
    
    @staticmethod
    def instancia(self, other):
        '''Instancia que comprueba las probabilidades de ganar de cada personaje
        Parameters
        ----------
        self: [Personaje]
            Objeto personaje que se quiere comparar
        other: [Personaje]
            Objeto personaje que se quiere comparar
        Returns
        ----------
        [float]
            Probabilidad de ganar del primer personaje
        '''
        if self > other:
            return 0.66
        elif self < other:
            return 0.33
        else:
            return 0.50
        
    @staticmethod
    def opciones_y_accion(oponente: str, probabilidad: float):
        '''Metodo que da las opciones al jugador y le pide su respuesta
        Parameters
        ----------
        oponente: [str]
            Nombre del contrincante
        probabilidad: [float]
            Probabilidad de ganar del personaje
        Returns
        ----------
        [int]
            Es la accion que el usuario decide 1 o 2 son validos
        '''
        print(f"Oh no! Ha aparecido un {oponente}")
        print(f"Con tu nivel actual, tienes {probabilidad*100}% de probabilidades de ganarle al {oponente}\n")

        print(f"En caso de ganarle, recibiras 50 puntos de experiencia y el {oponente} perdera 30")
        print(f"En caso de perder, perderas 30 puntos de experiencia y el {oponente} ganara 50\n")

        print("Deseas")
        print("1. Atacar")
        print("2. Huir")
        return int(input())
    
    @staticmethod
    def resultado(oponente: str, accion: int, probabilidad: float):
        '''Metodo que responde si el personaje gana contra su contrincante o no
        Parameters
        ----------
        oponente: [str]
            Nombre del contrincante
        accion: [int]
            Accion a tomar, aceptadas 2 y 1
        probabilidad: [float]
            Probabilidad de ganar del personaje
        Returns
        ----------
        [int]
            Devuelve 0 si escapa, 1 si gana o -1 si pierde
        '''
        if accion == 2:
            print(f"El {oponente} ha quedado atras")
            return 0
        elif accion == 1:
            combate = probabilidad - random.uniform(0.0, 1.0)
            if combate >= 0:
                print(f"Ganaste contra {oponente}")
                return 1
            else:
                print(f"Perdiste contra {oponente}")
                return -1


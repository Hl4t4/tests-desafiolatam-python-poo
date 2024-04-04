from abc import ABC, abstractmethod
from npc import NPC
import random

class Personaje(ABC):
    def __init__(self, HP:int, ATK:int, DF:int, **kwargs):
        super().__init__(**kwargs)
        self.__HP = HP
        self.__ATK = ATK
        self.__DF = DF

    @abstractmethod
    def atacar(self) -> int:
        pass

    @abstractmethod
    def defender(self, ataque:int):
        pass

    @property
    def hp(self):
        return self.__HP
    
    @hp.setter
    def hp(self, HP:int):
        self.__HP = HP
    
    @property
    def atk(self):
        return self.__ATK
    
    @property
    def df(self):
        return self.__DF
    
    

class Jugador(Personaje):
    def __init__(self, hp: int, atk: int, df: int, arma: str = None) -> None:
        super().__init__(hp, atk, df)
        self.__arma = arma

    @property
    def arma(self):
        return self.__arma

    def atacar(self):
        if (self.arma != None):
            ataque = self.atk + random.randint(1, 5)
            print(f"Atacas a tu oponente por {ataque} ATK")
            return ataque
        else:
            print(f"Atacas a tu oponente por {self.atk} ATK")
            return self.atk
    
    def defender(self, ataque:int):
        defensa = random.randint(1, self.df)
        dano = max(ataque - defensa, 1)
        print(f"Te defiendes por un total de {defensa} DF")
        print(f"Recibes {dano} de daño")
        self.hp = self.hp - dano
        print(f"Tu nueva vida es {self.hp} HP\n")

class Monstruo(Personaje, NPC):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def atacar(self):
        ataque = self.atk + int(self.hp * 0.01)
        print(f"El monstruo te ataca por {ataque} ATK")
        return ataque
    
    def defender(self, ataque:int):
        defensa = self.df + int(self.hp * 0.001)
        dano = max(ataque - defensa, 1)
        print(f"El monstruo se defiende por un total de {defensa} DF")
        print(f"Recibe {dano} de daño")
        self.hp = self.hp - dano
        print(f"Su nueva vida es {self.hp} HP\n")
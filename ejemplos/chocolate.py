from sin_gluten import SinGluten
from abc import ABC, abstractmethod

class Chocolate(ABC):
    def __init__(self, porc_cacao: float) -> None:
        self.porc_cacao = self.validar_porc_cacao(porc_cacao)
        
    @abstractmethod
    def validar_porc_cacao(self, porc:float) -> float:
        pass

class ChocolateAmargo(Chocolate):
    def validar_porc_cacao(self, porc:float):
        return min(max(0.75, porc), 0.85)

class ChocolateAmargoSinGluten(ChocolateAmargo, SinGluten):
    pass

c = ChocolateAmargo(0.3)
print(c.porc_cacao)
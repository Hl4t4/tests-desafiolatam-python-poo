# archivo medicamento.py
class Medicamento():
    descuento = 0.05
    IVA = 0.18

    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    
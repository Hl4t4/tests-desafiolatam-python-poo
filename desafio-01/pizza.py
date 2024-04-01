import ingredientes

#Con verificacion
def agregar_ingrediente(tipo_ingrediente: str, ingredientes_posibles: list):
    print(f"Agregue uno de los siguientes {tipo_ingrediente}:")
    for ingrediente in ingredientes_posibles:
        print(f"{ingrediente}:")
    nuevo_ingrediente = input().capitalize()
    if nuevo_ingrediente in ingredientes_posibles:
        return nuevo_ingrediente
    else:
        print("Opcion incorrecta")
        return agregar_ingrediente(tipo_ingrediente, ingredientes_posibles)

#Sin verificacion
def agregar_ingrediente_unsafe(tipo_ingrediente: str, ingredientes_posibles: list):
    print(f"Agregue uno de los siguientes {tipo_ingrediente}:")
    for ingrediente in ingredientes_posibles:
        print(f"{ingrediente}:")
    return input().capitalize()

def comprobar_ingrediente_valido(ingrediente: str, ingredientes_posibles: list):
    return ingrediente in ingredientes_posibles

class Pizza():
    precio = 10000
    size = "Familiar"

    vegetales = []
    proteicos = []

    # pollo, vacuno, carne vegetal
    # tomate, aceitunas y champiñones

    @staticmethod
    def validar_de_lista(elemento: str, valores_posibles: list):
        return elemento in valores_posibles
    
    def pizza_valida(self):
        self.valida = True
        for proteico in self.proteicos:
            if not comprobar_ingrediente_valido(proteico, ingredientes.proteicos):
                self.valida = False
                return
        for vegetal in self.vegetales:
            if not comprobar_ingrediente_valido(vegetal, ingredientes.vegetales):
                self.valida = False
                return
        if not comprobar_ingrediente_valido(self.masa, ingredientes.masas):
                self.valida = False

    def realizar_pedido(self):
        # self.proteicos.append(agregar_ingrediente("ingredientes proteicos", ["Pollo", "Vacuno", "Carne Vegetal"]))
        # self.vegetales.append(agregar_ingrediente("ingredientes vegetales", ["tomate", "aceitunas", "Carne champiñones"]))
        # self.masa = agregar_ingrediente("tipos de masa", ["Tradicional", "Delgada"])
        self.proteicos.append(agregar_ingrediente_unsafe("ingredientes proteicos", ingredientes.proteicos))
        self.vegetales.append(agregar_ingrediente_unsafe("ingredientes vegetales", ingredientes.vegetales))
        self.masa = agregar_ingrediente_unsafe("tipos de masa", ingredientes.masas)

        self.pizza_valida()
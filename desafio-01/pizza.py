import ingredientes

    # #Con verificacion
    
    # def agregar_ingrediente(tipo_ingrediente: str, ingredientes_posibles: list):
    #     print(f"Agregue uno de los siguientes {tipo_ingrediente}:")
    #     for ingrediente in ingredientes_posibles:
    #         print(f"{ingrediente}:")
    #     nuevo_ingrediente = input().capitalize()
    #     if nuevo_ingrediente in ingredientes_posibles:
    #         return nuevo_ingrediente
    #     else:
    #         print("Opcion incorrecta")
    #         return agregar_ingrediente(tipo_ingrediente, ingredientes_posibles)

class Pizza():
    precio = 10000
    size = "Familiar"

    vegetales = []
    proteicos = []

    #Sin verificacion
    @staticmethod
    def agregar_ingrediente_unsafe(tipo_ingrediente: str, ingredientes_posibles: list):
        '''Metodo estatico que adquiere un nuevo ingrediente para la pizza
        Parameters
        ----------
        tipo_ingrediente: [str]
            El tipo de ingrediente con texto extra para mejorar usabilidad de usuario
        tipo_ingrediente: [list]
            Listado con ingredientes posibles
        Returns
        ----------
        [str]
            Ingrediente a agregar a la pizza
        '''
        print(f"Agregue uno de los siguientes {tipo_ingrediente}:")
        for ingrediente in ingredientes_posibles:
            print(f"{ingrediente}")
        return input().capitalize()
    
    @staticmethod
    def comprobar_ingrediente_valido(ingrediente: str, ingredientes_posibles: list):
        '''Metodo estatico que comprueba si un ingrediente es valido
        Parameters
        ----------
        ingrediente: [str]
            El ingrediente a comprobar si es valido
        tipo_ingrediente: [list]
            Listado con ingredientes posibles
        Returns
        ----------
        [bool]
            Booleano si el ingrediente es valido o no
        '''
        return ingrediente in ingredientes_posibles 

    # @staticmethod
    # def validar_de_lista(elemento: str, valores_posibles: list):
    #     return elemento in valores_posibles
    
    def pizza_valida(self):
        '''Metodo que comprueba si todos los ingredientes de la pizza son validos
        Parameters
        ----------
        self: [Object]
            Una pizza con sus ingredientes
        Returns
        ----------
        '''
        self.valida = True
        for proteico in self.proteicos:
            if not self.comprobar_ingrediente_valido(proteico, ingredientes.proteicos):
                self.valida = False
                return
        for vegetal in self.vegetales:
            if not self.comprobar_ingrediente_valido(vegetal, ingredientes.vegetales):
                self.valida = False
                return
        if not self.comprobar_ingrediente_valido(self.masa, ingredientes.masas):
                self.valida = False

    def realizar_pedido(self):
        '''Metodo que agrega los ingredientes a una pizza y luego verifica si es una pizza valida
        Parameters
        ----------
        self: [Object]
            Una pizza con sus ingredientes
        Returns
        ----------
        '''
        # self.proteicos.append(agregar_ingrediente("ingredientes proteicos", ["Pollo", "Vacuno", "Carne Vegetal"]))
        # self.vegetales.append(agregar_ingrediente("ingredientes vegetales", ["tomate", "aceitunas", "Carne champiñones"]))
        # self.masa = agregar_ingrediente("tipos de masa", ["Tradicional", "Delgada"])
        self.proteicos.append(self.agregar_ingrediente_unsafe("ingredientes proteicos", ingredientes.proteicos))
        self.vegetales.append(self.agregar_ingrediente_unsafe("ingredientes vegetales", ingredientes.vegetales))
        self.vegetales.append(self.agregar_ingrediente_unsafe("ingredientes vegetales", ingredientes.vegetales))
        self.masa = self.agregar_ingrediente_unsafe("tipos de masa", ingredientes.masas)

        self.pizza_valida()
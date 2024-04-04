class Te():
    sabor = int
    tiempo = int
    descripcion = str
    formato = int

    @staticmethod
    def tiempo_y_recomendacion (sabor: int):
        '''Metodo estatico que obtiene el tiempo y recomendacion segun el tipo de te
        Parameters
        ----------
        sabor: [int]
            Int con el valor del tipo de te, que puede ser 1, 2 o 3
        Returns
        ----------
        [tuple]
            Tupa con el tiempo de preparacion y recomendacion segun tipo de te
        '''
        #Te negro
        if sabor == 1:
            return 3, "Se recomienda consumir al desayuno"
        #Te verde
        elif sabor == 2:
            return 5, "Se recomienda consumir al medio dia"
        #Agua de hierbas
        elif sabor == 3:
            return 6, "Se recomienda consumir al atardecer"
        else:
            return 0, "Valor no valido"
    
    @staticmethod
    def precio (formato: int):
        '''Metodo estatico que obtiene precio segun el formato en el que viene el te
        Parameters
        ----------
        sabor: [int]
            Int con el valor del formato de te, que puede ser 300 o 500
        Returns
        ----------
        [int]
            Int con el precio del te
        '''
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        else:
            return 0

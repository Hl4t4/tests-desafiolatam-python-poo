class Te():
    sabor = int
    tiempo = int
    descripcion = str
    formato = int

    @staticmethod
    def tiempo_y_recomendacion (sabor: int):
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
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        else:
            return 0

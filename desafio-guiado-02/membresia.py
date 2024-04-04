from abc import ABC, abstractmethod

#Clase Padre de todas
class Membresia(ABC):
    def __init__(self, correo_suscriptor:str, numero_tarjeta:str):
        '''Constructor de la clase Membresia
        Parameters
        ----------
        self: [Membresia]
            Objeto con propiedades de objeto Membresia, puede ser uno de los hijos
        correo_suscriptor: [str]
            Correo de la persona que se suscribe al servicio
        numero_tarjeta: [str]
            Numero de la tarjeta de la persona que se suscribe al servicio
        Returns
        ----------
        '''
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        '''Getter del correo del suscriptor
        Parameters
        ----------
        self: [Membresia]
            Objeto con propiedades de objeto Membresia, puede ser uno de los hijos
        Returns
        ----------
        [str]
            Correo de la persona que esta suscrita al servicio
        '''
        return self.__correo_suscriptor
    
    @property
    def numero_tarjeta(self):
        '''Getter del numero de la tarjeta
        Parameters
        ----------
        self: [Membresia]
            Objeto con propiedades de objeto Membresia, puede ser uno de los hijos
        Returns
        ----------
        [str]
            Numero de la tarjeta de la persona que esta suscrita al servicio
        '''
        return self.__numero_tarjeta
    
    @property
    def costo(self):
        '''Getter del costo de suscripcion
        Parameters
        ----------
        self: [Membresia]
            Objeto con propiedades de objeto Membresia, puede ser uno de los hijos
        Returns
        ----------
        [int]
            Costo del servicio suscrito
        '''
        return self.__costo
    
    @costo.setter
    def costo(self, costo:int):
        '''Setter del costo de suscripcion
        Parameters
        ----------
        self: [Membresia]
            Objeto con propiedades de objeto Membresia, puede ser uno de los hijos
        costo: [int]
            Valor del costo de suscripcion
        Returns
        ----------
        '''
        self.__costo = costo

    @property
    def dispositivos(self):
        '''Getter de la cantidad de dispositivos
        Parameters
        ----------
        self: [Membresia]
            Objeto con propiedades de objeto Membresia, puede ser uno de los hijos
        Returns
        ----------
        [int]
            Cantidad de dispositivos que puede conectar simultaneamente el suscriptor
        '''
        return self.__dispositivos
    
    @dispositivos.setter
    def dispositivos(self, dispositivos:int):
        '''Setter de la cantidad de dispositivos
        Parameters
        ----------
        self: [Membresia]
            Objeto con propiedades de objeto Membresia, puede ser uno de los hijos
        dispositivos: [int]
            Cantidad de dispositivos que puede usar simultaneamente el suscriptor
        Returns
        -------
        '''
        self.__dispositivos = dispositivos
    
    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia:int):
        '''Metodo abstracto para cambiar la suscripcion
        Parameters
        ----------
        self: [Membresia]
            Objeto con propiedades de objeto Membresia, puede ser uno de los hijos
        nueva_membresia: [int]
            El numero correspondiente al tipo de suscripcion
        Returns
        -------
        '''
        pass

    def _crear_nueva_membresia(self, nueva_membresia:int):
        '''Metodo protected para crear una nueva membresia
        Parameters
        ----------
        self: [Membresia]
            Objeto con propiedades de objeto Membresia, puede ser uno de los hijos
        nueva_membresia: [int]
            El numero correspondiente al tipo de suscripcion
        Returns
        -------
        [Basica/Familiar/SinConexion/Pro]
            Nuevo objeto de clase hija de Membresia
        '''
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
        
class Gratis(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        '''Constructor de la clase Gratis
        Parameters
        ----------
        self: [Gratis]
            Objeto con propiedades de objeto Gratis
        correo_suscriptor: [str]
            Correo de la persona que se suscribe al servicio
        numero_tarjeta: [str]
            Numero de la tarjeta de la persona que se suscribe al servicio
        Returns
        ----------
        '''
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 0
        self.dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        '''Metodo para cambiar de membresia
        Parameters
        ----------
        self: [Gratis]
            Objeto con propiedades de objeto Gratis
        nueva_membresia: [int]
            El numero correspondiente al tipo de suscripcion
        Returns
        -------
        [Basica/Familiar/SinConexion/Pro]
            Nuevo objeto de clase hija de Membresia
        '''
        if nueva_membresia >= 1 and nueva_membresia <= 4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
        
class Basica(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        '''Constructor de la clase Basica
        Parameters
        ----------
        self: [Basica]
            Objeto con propiedades de objeto Basica, puede tambien Familiar, Pro o SinConexion
        correo_suscriptor: [str]
            Correo de la persona que se suscribe al servicio
        numero_tarjeta: [str]
            Numero de la tarjeta de la persona que se suscribe al servicio
        Returns
        ----------
        '''
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 3000
        self.dispositivos = 2
        #Se agregan los dias gratis dependiendo del tipo de suscripcion
        if isinstance(self, Pro):
            self.__dias = 15
        elif isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias = 7

    @property
    def dias(self):
        '''Getter de los dias gratuitos del suscriptor
        Parameters
        ----------
        self: [Basica]
            Objeto con propiedades de objeto Basica, puede tambien Familiar, Pro o SinConexion
        Returns
        ----------
        [int]
            Dias de servicio gratuito
        '''
        return self.__dias
    
    #Se puede agregar el setter y cambiar como se hace el constructor tambien

    def cambiar_suscripcion(self, nueva_membresia: int):
        '''Metodo para cambiar de membresia
        Parameters
        ----------
        self: [Basica]
            Objeto con propiedades de objeto Basica, puede tambien Familiar, Pro o SinConexion
        nueva_membresia: [int]
            El numero correspondiente al tipo de suscripcion
        Returns
        -------
        [Familiar/SinConexion/Pro]
            Nuevo objeto de clase hija de Membresia
        '''
        if nueva_membresia >= 2 and nueva_membresia <= 4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
        
    def cancelar_suscripcion(self):
        '''Metodo para cancelar suscripcion y volver a cuenta gratuita
        Parameters
        ----------
        self: [Basica]
            Objeto con propiedades de objeto Basica, puede tambien Familiar, Pro o SinConexion
        Returns
        -------
        [Gratis]
            Membresia de costo 0
        '''
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

class Familiar(Basica):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        '''Constructor de la clase Familiar
        Parameters
        ----------
        self: [Familiar]
            Objeto con propiedades de objeto Familiar o Pro
        correo_suscriptor: [str]
            Correo de la persona que se suscribe al servicio
        numero_tarjeta: [str]
            Numero de la tarjeta de la persona que se suscribe al servicio
        Returns
        ----------
        '''
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 5000
        self.dispositivos = 5

    def cambiar_suscripcion(self, nueva_membresia: int):
        '''Metodo para cambiar de membresia
        Parameters
        ----------
        self: [Familiar]
            Objeto con propiedades de objeto Familiar, puede tambien Pro o SinConexion
        nueva_membresia: [int]
            El numero correspondiente al tipo de suscripcion
        Returns
        -------
        [Basica/SinConexion/Pro]
            Nuevo objeto de clase hija de Membresia
        '''
        if nueva_membresia == 1 or nueva_membresia == 3 or nueva_membresia == 4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

    #CONTROL PARENTAL POR DEFINIR 
    def control_parental(self):
        pass
        
class SinConexion(Basica):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        '''Constructor de la clase Familiar
        Parameters
        ----------
        self: [SinConexion]
            Objeto con propiedades de objeto SinConexion o Pro
        correo_suscriptor: [str]
            Correo de la persona que se suscribe al servicio
        numero_tarjeta: [str]
            Numero de la tarjeta de la persona que se suscribe al servicio
        Returns
        ----------
        '''
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 3500
        self.dispositivos = 2

    def cambiar_suscripcion(self, nueva_membresia: int):
        '''Metodo para cambiar de membresia
        Parameters
        ----------
        self: [SinConexion]
            Objeto con propiedades de objeto SinConexion, puede tambien Pro
        nueva_membresia: [int]
            El numero correspondiente al tipo de suscripcion
        Returns
        -------
        [Basica/Familiar/Pro]
            Nuevo objeto de clase hija de Membresia
        '''
        if nueva_membresia == 1 or nueva_membresia == 2 or nueva_membresia == 4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

    #AUMENTAR CONTENIDO DISPONIBLE POR DEFINIR 
    def agregar_contenido(self):
        pass

class Pro(Familiar, SinConexion):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        '''Constructor de la clase Pro
        Parameters
        ----------
        self: [Pro]
            Objeto con propiedades de objeto Pro
        correo_suscriptor: [str]
            Correo de la persona que se suscribe al servicio
        numero_tarjeta: [str]
            Numero de la tarjeta de la persona que se suscribe al servicio
        Returns
        ----------
        '''
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 7500
        self.dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia: int):
        '''Metodo para cambiar de membresia
        Parameters
        ----------
        self: [Pro]
            Objeto con propiedades de objeto Pro
        nueva_membresia: [int]
            El numero correspondiente al tipo de suscripcion
        Returns
        -------
        [Basica/Familiar/SinConexion]
            Nuevo objeto de clase hija de Membresia
        '''
        if nueva_membresia == 1 or nueva_membresia == 2 or nueva_membresia == 3:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
        
prueba = Pro("correo@correo.cl", 500)
print(prueba.dias)

prueba = prueba.cambiar_suscripcion(2)
print(prueba.dias)

prueba = prueba.cancelar_suscripcion()
print(prueba.costo)
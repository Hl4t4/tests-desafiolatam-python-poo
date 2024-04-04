class Monitor():
    def __init__(self, resolucion:str) -> None:
        self.resolucion = resolucion

class Televisor():
    pass

class MonitorLED(Monitor):
    pass

class Monitor2en1(Monitor, Televisor):
    def __init__(self, resolucion: str) -> None:
        super().__init__(resolucion)
    pass
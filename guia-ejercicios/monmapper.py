import requests 

class MonMapper():
    def __init__(self, base_url: str) -> None:
        self.__base_url = base_url

    @property
    def base_url(self) -> str:
        return self.__base_url
    
    @base_url.setter
    def base_url(self, base_url) -> None:
        self.__base_url = base_url

class PokemonMapper(MonMapper):
    def __init__(self, base_url: str, limit: int = 20) -> None:
        super().__init__(base_url)
        self.__limit = limit
    
    @property
    def limit(self) -> int:
        return self.__limit
    
    @limit.setter
    def limit(self, limit) -> None:
        self.__limit = limit

    def obtener_mon_por_nombre(self, nombre: str) -> dict:
        respuesta = requests.get(f"{self.base_url}/{nombre}?limit={self.limit}")

class DigimonMapper(MonMapper):
    def __init__(self, base_url: str) -> None:
        super().__init__(base_url)

    def obtener_mon_por_nombre(self, nombre: str) -> dict:
        respuesta = requests.get(f"{self.base_url}/{nombre}"
)

print(requests)
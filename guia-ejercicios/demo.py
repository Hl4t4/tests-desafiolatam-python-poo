from monmapper import PokemonMapper, DigimonMapper

for mapper in mappers:
    if isinstance(mapper, PokemonMapper):
        print("Obteniendo listado de Pokemones...")
    elif isinstance(mapper, DigimonMapper):
        print("Obteniendo listado de Digimones...")
    mons += mapper.obtener_todos_los_mon()
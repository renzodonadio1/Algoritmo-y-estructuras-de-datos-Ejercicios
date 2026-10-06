from list_ import List

# Estructura de datos de prueba
entrenadores_data = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 4,
        "batallas_perdidas": 10,
        "batallas_ganadas": 50,
        "pokemons": [
            {"nombre": "Pikachu", "nivel": 88, "tipo": "Eléctrico", "subtipo": None},
            {"nombre": "Charizard", "nivel": 85, "tipo": "Fuego", "subtipo": "Volador"},
            {"nombre": "Charizard", "nivel": 70, "tipo": "Fuego", "subtipo": "Volador"},  # Repetido para probar i
            {"nombre": "Bulbasaur", "nivel": 60, "tipo": "Planta", "subtipo": "Veneno"}
        ]
    },
    {
        "nombre": "Misty",
        "torneos_ganados": 2,
        "batallas_perdidas": 15,
        "batallas_ganadas": 35,
        "pokemons": [
            {"nombre": "Starmie", "nivel": 75, "tipo": "Agua", "subtipo": "Psíquico"},
            {"nombre": "Psyduck", "nivel": 40, "tipo": "Agua", "subtipo": None},
            {"nombre": "Wingull", "nivel": 45, "tipo": "Agua", "subtipo": "Volador"}
        ]
    },
    {
        "nombre": "Cynthia",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 95,
        "pokemons": [
            {"nombre": "Garchomp", "nivel": 92, "tipo": "Dragón", "subtipo": "Tierra"},
            {"nombre": "Lucario", "nivel": 88, "tipo": "Lucha", "subtipo": "Acero"},
            {"nombre": "Terrakion", "nivel": 85, "tipo": "Roca", "subtipo": "Lucha"}
        ]
    },
    {
        "nombre": "Red",
        "torneos_ganados": 5,
        "batallas_perdidas": 2,
        "batallas_ganadas": 80,
        "pokemons": [
            {"nombre": "Snorlax", "nivel": 85, "tipo": "Normal", "subtipo": None},
            {"nombre": "Lapras", "nivel": 80, "tipo": "Agua", "subtipo": "Hielo"},
            {"nombre": "Tyrantrum", "nivel": 78, "tipo": "Roca", "subtipo": "Dragón"}
        ]
    }
]

# Cargar la lista de listas
lista_entrenadores = List()
lista_entrenadores.add_criterion("nombre", lambda e: e["nombre"].lower())
lista_entrenadores.add_criterion("torneos", lambda e: e["torneos_ganados"])

for e_data in entrenadores_data:
    sublista_pokemons = List()
    sublista_pokemons.add_criterion("nombre", lambda p: p["nombre"].lower())
    sublista_pokemons.add_criterion("nivel", lambda p: p["nivel"])
    
    for p in e_data["pokemons"]:
        sublista_pokemons.append(p)
        
    entrenador = {
        "nombre": e_data["nombre"],
        "torneos_ganados": e_data["torneos_ganados"],
        "batallas_perdidas": e_data["batallas_perdidas"],
        "batallas_ganadas": e_data["batallas_ganadas"],
        "pokemons": sublista_pokemons  # Sublista de Pokémon
    }
    lista_entrenadores.append(entrenador)


print("--- EJERCICIO 15: ENTRENADORES POKÉMON ---")

# a. Cantidad de Pokémon de un determinado entrenador
def cantidad_pokemons(lista, nombre_entrenador):
    pos = lista.search(nombre_entrenador.lower(), "nombre")
    if pos is not None:
        return lista[pos]["pokemons"].size()
    return 0

print("\na. Cantidad de Pokémon de Ash Ketchum:")
print(f"   Ash tiene {cantidad_pokemons(lista_entrenadores, 'Ash Ketchum')} Pokémon.")


# b. Listar los entrenadores que hayan ganado más de 3 torneos
print("\nb. Entrenadores con más de 3 torneos ganados:")
for e in lista_entrenadores:
    if e["torneos_ganados"] > 3:
        print(f"   - {e['nombre']} ({e['torneos_ganados']} torneos)")


# c. Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
print("\nc. Pokémon de mayor nivel del entrenador con más torneos:")
lista_entrenadores.sort_by_criterion("torneos")
entrenador_top = lista_entrenadores[-1]  # El último tras ordenar es el máximo

sublista = entrenador_top["pokemons"]
sublista.sort_by_criterion("nivel")
pokemon_top = sublista[-1]

print(f"   Entrenador top: {entrenador_top['nombre']}")
print(f"   Pokémon mayor nivel: {pokemon_top['nombre']} (Nivel {pokemon_top['nivel']})")


# d. Mostrar todos los datos de un entrenador y sus Pokémon
print("\nd. Datos completos de Misty:")
pos_misty = lista_entrenadores.search("misty", "nombre")
if pos_misty is not None:
    e = lista_entrenadores[pos_misty]
    print(f"   Entrenador: {e['nombre']} | Torneos: {e['torneos_ganados']} | "
          f"Ganadas: {e['batallas_ganadas']} | Perdidas: {e['batallas_perdidas']}")
    print("   Pokémon:")
    for p in e["pokemons"]:
        subt = f" / {p['subtipo']}" if p['subtipo'] else ""
        print(f"     - {p['nombre']} (Nivel {p['nivel']}) - Tipo: {p['tipo']}{subt}")


# e. Entrenadores con porcentaje de batallas ganadas > 79%
print("\ne. Entrenadores con más del 79% de batallas ganadas:")
for e in lista_entrenadores:
    total_batallas = e["batallas_ganadas"] + e["batallas_perdidas"]
    if total_batallas > 0:
        porcentaje = (e["batallas_ganadas"] / total_batallas) * 100
        if porcentaje > 79:
            print(f"   - {e['nombre']}: {porcentaje:.2f}% de victorias")


# f. Entrenadores con Pokémon tipo (Fuego y Planta) O (Agua y Volador)
print("\nf. Entrenadores con Pokémon de tipo Fuego/Planta o Agua/Volador:")
for e in lista_entrenadores:
    tiene_fuego = False
    tiene_planta = False
    tiene_agua_volador = False
    
    for p in e["pokemons"]:
        if p["tipo"] == "Fuego":
            tiene_fuego = True
        if p["tipo"] == "Planta":
            tiene_planta = True
        if (p["tipo"] == "Agua" and p["subtipo"] == "Volador") or (p["tipo"] == "Volador" and p["subtipo"] == "Agua"):
            tiene_agua_volador = True
            
    if (tiene_fuego and tiene_planta) or tiene_agua_volador:
        print(f"   - {e['nombre']}")


# g. Promedio de nivel de los Pokémon de un entrenador
def promedio_nivel(lista, nombre_entrenador):
    pos = lista.search(nombre_entrenador.lower(), "nombre")
    if pos is not None:
        pokemons = lista[pos]["pokemons"]
        if pokemons.size() > 0:
            suma_niveles = sum(p["nivel"] for p in pokemons)
            return suma_niveles / pokemons.size()
    return 0

print("\ng. Promedio de nivel de los Pokémon de Cynthia:")
prom = promedio_nivel(lista_entrenadores, "Cynthia")
print(f"   Promedio: {prom:.2f}")


# h. Cuántos entrenadores tienen a un determinado Pokémon
def cantidad_entrenadores_con_pokemon(lista, nombre_pokemon):
    contador = 0
    for e in lista:
        if e["pokemons"].search(nombre_pokemon.lower(), "nombre") is not None:
            contador += 1
    return contador

pokemon_buscar = "Charizard"
print(f"\nh. Cantidad de entrenadores con {pokemon_buscar}:")
print(f"   {cantidad_entrenadores_con_pokemon(lista_entrenadores, pokemon_buscar)} entrenador(es).")


# i. Entrenadores que tienen Pokémon repetidos
print("\ni. Entrenadores con Pokémon repetidos:")
for e in lista_entrenadores:
    nombres_pkmn = [p["nombre"].lower() for p in e["pokemons"]]
    if len(nombres_pkmn) != len(set(nombres_pkmn)):
        print(f"   - {e['nombre']} tiene Pokémon repetidos.")


# j. Entrenadores que tengan a Tyrantrum, Terrakion o Wingull
print("\nj. Entrenadores que tienen a Tyrantrum, Terrakion o Wingull:")
objetivos = ["tyrantrum", "terrakion", "wingull"]
for e in lista_entrenadores:
    for p in e["pokemons"]:
        if p["nombre"].lower() in objetivos:
            print(f"   - {e['nombre']} tiene a {p['nombre']}")
            break


# k. Determinar si un entrenador "X" tiene al Pokémon "Y" y mostrar datos de ambos
def consultar_entrenador_pokemon(lista, nombre_e, nombre_p):
    pos_e = lista.search(nombre_e.lower(), "nombre")
    if pos_e is None:
        print(f"   El entrenador '{nombre_e}' no fue encontrado.")
        return

    entrenador = lista[pos_e]
    pos_p = entrenador["pokemons"].search(nombre_p.lower(), "nombre")
    
    if pos_p is not None:
        pokemon = entrenador["pokemons"][pos_p]
        print(f"\n   [COINCIDENCIA ENCONTRADA!]")
        print(f"   Datos del Entrenador: {entrenador['nombre']} | Torneos: {entrenador['torneos_ganados']}")
        subt = f" / {pokemon['subtipo']}" if pokemon['subtipo'] else ""
        print(f"   Datos del Pokémon: {pokemon['nombre']} | Nivel: {pokemon['nivel']} | Tipo: {pokemon['tipo']}{subt}")
    else:
        print(f"   El entrenador {entrenador['nombre']} NO tiene a {nombre_p}.")

print("\nk. Consulta de entrenador y Pokémon (Ejemplo 1):")
consultar_entrenador_pokemon(lista_entrenadores, "Ash Ketchum", "Pikachu")

print("\nk. Consulta de entrenador y Pokémon (Ejemplo 2):")
consultar_entrenador_pokemon(lista_entrenadores, "Misty", "Charizard")
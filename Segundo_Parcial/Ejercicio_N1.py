from pokemon_data import pokemons
from tree import BinaryTree, insert_node, inorden, por_nivel

# Inicialización de los tres árboles requeridos (por nombre, número y tipo)
tree_name = None
tree_number = None
tree_type = None

# Función auxiliar para insertar en el árbol
def insert_node_type(root, type_key, data):
    if root is None:
        return BinaryTree(type_key, [data])
    if root.value == type_key:
        root.data.append(data)
    elif type_key < root.value:
        root.left = insert_node_type(root.left, type_key, data)
    else:
        root.right = insert_node_type(root.right, type_key, data)
    return root

# Carga de datos en los árboles (al menos 100 Pokémons, el archivo trae 120+)

for p in pokemons:
    tree_name = insert_node(tree_name, p["name"].lower(), p)
    tree_number = insert_node(tree_number, p["number"], p)
    for t in p["types"]:
        tree_type = insert_node_type(tree_type, t.lower(), p)

print(f"Total de Pokémons cargados: {len(pokemons)}")

# 1. Búsqueda por proximidad en el árbol de nombres

def search_by_proximity(root, term, results):
    if root is not None:
        search_by_proximity(root.left, term, results)
        if term in root.value:
            results.append(root.data)
        search_by_proximity(root.right, term, results)

print("\nBúsqueda por proximidad ('bul')")
resultados_proximidad = []
search_by_proximity(tree_name, "bul", resultados_proximidad)
for p in resultados_proximidad:
    print(f"-> {p['name']} (Nº {p['number']}) | Tipos: {p['types']} | Debilidades: {p['weaknesses']} | Mega: {p['has_mega_evolution']} | Gigamax: {p['has_gigamax']}")

# 2. Nombres de Pokémons de tipos específicos: fantasma, fuego, acero, eléctrico

def get_pokemons_by_type(root, target_type):
    if root is None:
        return []
    if root.value == target_type:
        return root.data
    elif target_type < root.value:
        return get_pokemons_by_type(root.left, target_type)
    else:
        return get_pokemons_by_type(root.right, target_type)

print("\nPokémons de tipos específicos")
for t_buscado in ["fantasma", "fuego", "acero", "eléctrico"]:
    lista = get_pokemons_by_type(tree_type, t_buscado)
    nombres = [p["name"] for p in lista]
    print(f"Tipo {t_buscado}: {nombres}")

# 3. Listados (ascendente por número y por nivel por nombre)

print("\nListado en orden ascendente por número")
inorden(tree_number)

print("\nListado por nivel por nombre")
por_nivel(tree_name)

# 4. Pokémons débiles frente a Jolteon, Lycanroc y Tyrantrum

def search_weaknesses(root, target_weakness, results):
    if root is not None:
        search_weaknesses(root.left, target_weakness, results)
        if target_weakness in [w.lower() for w in root.data["weaknesses"]]:
            if root.data not in results:
                results.append(root.data)
        search_weaknesses(root.right, target_weakness, results)

print("\nPokémons débiles frente a Jolteon (eléctrico), Lycanroc (roca) y Tyrantrum (roca)")
for atacante, tipo_ataque in [("Jolteon", "eléctrico"), ("Lycanroc", "roca"), ("Tyrantrum", "roca")]:
    debiles = []
    search_weaknesses(tree_number, tipo_ataque, debiles)
    print(f"Débiles a {atacante} (ataque tipo {tipo_ataque}): {[p['name'] for p in debiles]}")

# 5. Cantidad de Pokémons por tipo, con Mega y con Gigamax

print("\nConteo por Tipo")
def contar_tipos(root):
    if root is not None:
        contar_tipos(root.left)
        print(f"Tipo '{root.value}': {len(root.data)} pokémons")
        contar_tipos(root.right)

contar_tipos(tree_type)

conteo_mega = 0
conteo_gigamax = 0

def contar_caracteristicas(root):
    global conteo_mega, conteo_gigamax
    if root is not None:
        contar_caracteristicas(root.left)
        if root.data["has_mega_evolution"]:
            conteo_mega += 1
        if root.data["has_gigamax"]:
            conteo_gigamax += 1
        contar_caracteristicas(root.right)

contar_caracteristicas(tree_number)
print(f"\nPokémons con Megaevolución: {conteo_mega}")
print(f"Pokémons con forma Gigamax: {conteo_gigamax}")
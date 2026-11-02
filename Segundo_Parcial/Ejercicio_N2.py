from star_wars_data import star_wars_characters, star_wars_relationships
from graph import Graph

# Inicializar grafo no dirigido
g = Graph(is_dir=False)

# Cargar vértices (personajes con sus episodios almacenados en other_values)
for char in star_wars_characters:
    g.add_vertex(char["name"], other_values={"episodes": char["episodes"]})

# Cargar aristas (peso = cantidad de episodios compartidos)
for rel in star_wars_relationships:
    g.add_edge(rel["weight"], rel["origin"], rel["destination"])

print("Grafo de Star Wars cargado correctamente")

# 1. Número máximo de episodios compartidos y sus pares

max_weight = -1
max_pairs = []
checked_pairs = set()

for vertex in g:
    origin = vertex.value
    for edge in vertex.edges:
        dest = edge.destination
        weight = edge.weight
        pair = tuple(sorted([origin, dest]))
        if pair not in checked_pairs:
            checked_pairs.add(pair)
            if weight > max_weight:
                max_weight = weight
                max_pairs = [(origin, dest)]
            elif weight == max_weight:
                max_pairs.append((origin, dest))

print(f"\n1. Máximo de episodios compartidos ({max_weight} episodios)")
print(f"Pares de personajes: {max_pairs}")

# 2. Personajes que aparecieron en los nueve episodios

print("\n2. Personajes en los 9 episodios de la saga ")
personajes_9_eps = [char["name"] for char in star_wars_characters if len(char["episodes"]) == 9]
print(personajes_9_eps)

# 3. Árbol de Expansión Mínimo (Kruskal) desde C-3PO, Yoda y Leia

print("\n3. Árbol de Expansión Mínimo (MST)")
for origen_mst in ["C-3PO", "Yoda", "Leia"]:
    min_tree = g.kruskal(origen_mst)
    print(f"\nMST desde {origen_mst}:")
    if isinstance(min_tree, str):
        for edge_str in min_tree.split(';'):
            if '-' in edge_str:
                parts = edge_str.split('-')
                if len(parts) >= 3:
                    u, v, w = parts[0], parts[1], parts[2]
                    print(f"   {u} -- {v} (Peso: {w})")
    else:
        print(min_tree)

# 4. Caminos más cortos (dijstra) entre C-3PO y R2-D2, y entre Yoda y Darth Vader

def resolver_dijkstra(grafo, origen, destino):
    if not grafo.exist_path(origen, destino):
        print(f"No existe camino entre {origen} y {destino}")
        return
    
    paths = grafo.dijkstra(origen)
    actual = destino
    peso_total = None
    camino_completo = []

    while paths.size() > 0:
        value = paths.pop()
        if value[0] == actual:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            actual = value[2]
    
    camino_completo.reverse()
    print(f"Camino de {origen} a {destino} -> {' -> '.join(camino_completo)} | Costo total (episodios): {peso_total}")

print("\n 4. Caminos más cortos (Dijkstra)")
resolver_dijkstra(g, "C-3PO", "R2-D2")
resolver_dijkstra(g, "Yoda", "Darth Vader")
from graph import Graph


def crear_grafo_a():
  """Crea el Grafo A (Red inicial con la impresora)."""
  g = Graph(is_dir=False)  # Punto h: Grafo no dirigido

  # Punto a: Definir vértices con su respectivo tipo
  equipos = {
      "Manjaro": "pc",
      "Red Hat": "notebook",
      "Debian": "notebook",
      "Arch": "notebook",
      "Fedora": "pc",
      "Guaraní": "servidor",
      "MongoDB": "servidor",
      "router 01": "router",
      "router 02": "router",
      "switch 01": "switch",
      "impresora": "impresora",
  }

  for nombre, tipo in equipos.items():
    g.add_vertex(nombre, {"tipo": tipo})

  # Conexiones de la red inicial (Grafo A)
  conexiones = [
      (2, "Manjaro", "switch 01"),
      (3, "Red Hat", "switch 01"),
      (4, "Debian", "router 01"),
      (2, "Arch", "router 02"),
      (1, "Fedora", "switch 01"),
      (5, "switch 01", "router 01"),
      (3, "router 01", "router 02"),
      (4, "router 02", "impresora"),  # Conexión inicial de la impresora
      (6, "router 01", "Guaraní"),
      (4, "router 02", "MongoDB"),
  ]

  for peso, origen, destino in conexiones:
    g.add_edge(peso, origen, destino)

  return g


def crear_grafo_b():
  """Crea el Grafo B (Red modificada: impresora conectada al router 02 - Punto g)."""
  g = crear_grafo_a()
  # Punto g: Cambiar la conexión de la impresora al router 02
  g.delete_edge("router 02", "impresora")
  g.add_edge(2, "router 02", "impresora")
  return g


def obtener_camino_dijkstra(g, origen, destino):
  """Función auxiliar para reconstruir el camino y costo a partir del Stack de Dijkstra."""
  stack_res = g.dijkstra(origen)
  info_nodos = {}
  while stack_res.size() > 0:
    item = stack_res.pop()
    nombre = item[0]
    costo = item[1]
    predecesor = item[2]
    info_nodos[nombre] = {"costo": costo, "predecesor": predecesor}

  if destino not in info_nodos or info_nodos[destino]["costo"] == float("inf"):
    return [], float("inf")

  costo_total = info_nodos[destino]["costo"]
  camino = []
  actual = destino
  while actual is not None:
    camino.insert(0, actual)
    actual = info_nodos[actual]["predecesor"]

  return camino, costo_total


# Resolución de Tareas

def resolver_barridos(g, nombre_grafo):
  """Punto b y g: Barridos en profundidad y amplitud desde las 3 notebooks."""
  print(f"\n=== BARRIDOS ({nombre_grafo}) ===")
  notebooks = ["Red Hat", "Debian", "Arch"]
  for nb in notebooks:
    print(f"\nPartiendo desde notebook: {nb}")
    print("  - DFS (Profundidad - deep_show):")
    g.deep_show(nb)
    print("  - BFS (Amplitud - amplitude_show):")
    g.amplitude_show(nb)


def resolver_caminos_impresora(g):
  """Punto c: Camino más corto desde PCs a la impresora."""
  print("\n=== CAMINO MÁS CORTO A IMPRESORA ===")
  pcs = ["Manjaro", "Red Hat", "Fedora"]
  for pc in pcs:
    camino, costo = obtener_camino_dijkstra(g, pc, "impresora")
    print(
        f"De {pc} a impresora -> Camino: {camino} | Costo total (latencia):"
        f" {costo}"
    )


def resolver_arbol_expansion(g):
  """Punto d: Árbol de Expansión Mínima."""
  print("\n=== ÁRBOL DE EXPANSIÓN MÍNIMA (AEM) ===")
  eem = g.kruskal("Manjaro")
  print(eem)


def resolver_pc_a_guarani(g):
  """Punto e: PC (no notebook) con el camino más corto al servidor 'Guaraní'."""
  print("\n=== PC MÁS CERCANA A SERVIDOR 'GUARANÍ' ===")
  pcs = [
      v.value
      for v in g
      if v.other_values and v.other_values.get("tipo") == "pc"
  ]

  menor_costo = float("inf")
  mejor_pc = None
  mejor_camino = None

  for pc in pcs:
    camino, costo = obtener_camino_dijkstra(g, pc, "Guaraní")
    if costo < menor_costo:
      menor_costo = costo
      mejor_pc = pc
      mejor_camino = camino

  print(
      f"La PC seleccionada es '{mejor_pc}' con un costo de {menor_costo}."
      f" Camino: {mejor_camino}"
  )


def resolver_switch01_a_mongodb(g):
  """Punto f: Computadora del switch 01 con el camino más corto a 'MongoDB'."""
  print("\n=== EQUIPO DE SWITCH 01 MÁS CERCANO A 'MONGODB' ===")
  switch_node = None
  for v in g:
    if v.value == "switch 01":
      switch_node = v
      break

  if switch_node:
    computadoras = [
        edge.destination
        for edge in switch_node.edges
        if g.search(edge.destination, "value") is not None
        and g[g.search(edge.destination, "value")].other_values
        and g[g.search(edge.destination, "value")].other_values.get("tipo")
        in ["pc", "notebook"]
    ]

    menor_costo = float("inf")
    mejor_equipo = None
    mejor_camino = None

    for eq in computadoras:
      camino, costo = obtener_camino_dijkstra(g, eq, "MongoDB")
      if costo < menor_costo:
        menor_costo = costo
        mejor_equipo = eq
        mejor_camino = camino

    print(
        f"El equipo conectado al switch 01 es '{mejor_equipo}' con un costo de"
        f" {menor_costo}. Camino: {mejor_camino}"
    )


# --- Ejecución principal ---
if __name__ == "__main__":
  grafo_a = crear_grafo_a()
  grafo_b = crear_grafo_b()

  print("#          RESOLUCIÓN GRAFO A          #")

  resolver_barridos(grafo_a, "Grafo A")
  resolver_caminos_impresora(grafo_a)
  resolver_arbol_expansion(grafo_a)
  resolver_pc_a_guarani(grafo_a)
  resolver_switch01_a_mongodb(grafo_a)

  print("#          RESOLUCIÓN GRAFO B          #")

  resolver_barridos(grafo_b, "Grafo B (Impresora en Router 02)")
  resolver_caminos_impresora(grafo_b)
  resolver_arbol_expansion(grafo_b)
  resolver_pc_a_guarani(grafo_b)
  resolver_switch01_a_mongodb(grafo_b)
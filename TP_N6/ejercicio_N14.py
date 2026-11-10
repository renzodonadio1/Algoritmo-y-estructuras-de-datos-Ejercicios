from graph import Graph


def crear_grafo_casa():
  """Crea el grafo no dirigido para representar los ambientes de la casa (Ejercicio 14)."""
  g = Graph(is_dir=False)  # Punto a y d: Grafo no dirigido

  # Punto a: Vértices que representan los ambientes de la casa
  ambientes = [
      "cocina",
      "comedor",
      "cochera",
      "quincho",
      "baño 1",
      "baño 2",
      "habitación 1",
      "habitación 2",
      "sala de estar",
      "terraza",
      "patio",
  ]

  for ambiente in ambientes:
    g.add_vertex(ambiente)

  # Punto b: Cargar al menos tres aristas a cada vértice, y a dos de estas cinco.
  conexiones = [
      # (peso_metros, origen, destino)
      (3, "cocina", "comedor"),
      (5, "cocina", "baño 1"),
      (4, "cocina", "patio"),
      (6, "cocina", "sala de estar"),
      (4, "comedor", "sala de estar"),
      (5, "comedor", "habitación 1"),
      (3, "comedor", "baño 1"),
      (8, "cochera", "patio"),
      (6, "cochera", "quincho"),
      (7, "cochera", "sala de estar"),
      (5, "quincho", "patio"),
      (4, "quincho", "terraza"),
      (6, "quincho", "cochera"),
      (2, "baño 1", "habitación 1"),
      (3, "baño 1", "comedor"),
      (5, "baño 1", "cocina"),
      (3, "baño 2", "habitación 2"),
      (4, "baño 2", "terraza"),
      (5, "baño 2", "sala de estar"),
      (4, "habitación 1", "habitación 2"),
      (2, "habitación 1", "baño 1"),
      (5, "habitación 1", "comedor"),
      (4, "habitación 2", "baño 2"),
      (4, "habitación 2", "habitación 1"),
      (6, "habitación 2", "terraza"),
      (6, "sala de estar", "cocina"),
      (4, "sala de estar", "comedor"),
      (7, "sala de estar", "cochera"),
      (5, "sala de estar", "baño 2"),
      (3, "sala de estar", "terraza"),  # 1° vértice con 5 aristas
      (3, "terraza", "quincho"),
      (4, "terraza", "baño 2"),
      (6, "terraza", "habitación 2"),
      (3, "terraza", "sala de estar"),
      (4, "patio", "cocina"),
      (8, "patio", "cochera"),
      (5, "patio", "quincho"),
      (3, "patio", "comedor"),
      (6, "patio", "terraza"),  # 2° vértice con 5 aristas
  ]

  for peso, origen, destino in conexiones:
    pos_o = g.search(origen, "value")
    pos_d = g.search(destino, "value")
    if pos_o is not None and pos_d is not None:
      origen_nodo = g[pos_o]
      existe = any(edge.destination == destino for edge in origen_nodo.edges)
      if not existe:
        g.add_edge(peso, origen, destino)

  return g


def obtener_camino_dijkstra(g, origen, destino):
  """Función auxiliar para procesar el Stack de Dijkstra y obtener camino y costo."""
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


def calcular_metros_aem(aem_str):
  """Calcula la suma total de los metros de cable a partir del string devuelto por Kruskal."""
  total = 0
  if isinstance(aem_str, str):
    segmentos = aem_str.split(";")
    for seg in segmentos:
      if seg:
        partes = seg.split("-")
        if len(partes) >= 3:
          total += int(partes[-1])
  return total


# ==========================================
# Resolución de Tareas (Ejercicio 14)
# ==========================================
if __name__ == "__main__":
  g_casa = crear_grafo_casa()
  
  print("#      RESOLUCIÓN EJERCICIO 14 - CASA            #")
  
  # Punto a: ambientes de la casa (vértices del grafo)
  print("\n--- a. Ambientes de la casa (vértices del grafo) ---")
  print(ambientes := [v.value for v in g_casa])

  # Punto b: Verificación de grados (aristas) por vértice
  print("\n--- b. Verificación de conexiones por ambiente ---")
  for v in g_casa:
    print(f"  - {v.value}: {len(v.edges)} aristas conectadas")

  # Punto c: Árbol de Expansión Mínima y metros totales de cable
  print("\n--- c. Árbol de Expansión Mínima (Conectividad total) ---")
  aem_resultado = g_casa.kruskal("cocina")
  print("Estructura del AEM (Kruskal):")
  print(aem_resultado)
  metros_totales_aem = calcular_metros_aem(aem_resultado)
  print(
      f"Metros totales de cables necesarios para conectar todos los"
      f" ambientes: {metros_totales_aem} metros"
  )

  # Punto d: Camino más corto desde la habitación 1 hasta la sala de estar
  print(
      "\n--- d. Camino más corto para cable de red (Habitación 1 -> Sala de"
      " Estar) ---"
  )
  camino, metros_red = obtener_camino_dijkstra(
      g_casa, "habitación 1", "sala de estar"
  )
  print(f"Camino óptimo: {camino}")
  print(
      "Metros de cable de red necesarios (Habitación 1 a Sala de Estar):"
      f" {metros_red} metros"
  )
from queue import Queue

# Carga de datos de prueba
personajes_mcu = [
    {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
    {"nombre": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"}
]

cola_mcu = Queue()
for p in personajes_mcu:
    cola_mcu.arrive(p)

print("EJERCICIO 22: PERSONAJES DE MCU")

# Variables de control para las búsquedas específicas
personaje_capitana_marvel = None
superheroe_scott_lang = None
carol_danvers_encontrada = False
superheroe_carol = None

# Listas auxiliares para mostrar resultados acumulados
superheroes_femeninos = []
personajes_masculinos = []
coincidencias_s = []

# Procesamiento de la cola mediante ciclo rotativo
tamanio = cola_mcu.size()

for _ in range(tamanio):
    p = cola_mcu.attention()
    nombre = p["nombre"]
    superheroe = p["superheroe"]
    genero = p["genero"].upper()

    # a. Determinar el nombre del personaje de Capitana Marvel
    if superheroe.lower() == "capitana marvel":
        personaje_capitana_marvel = nombre

    # b. Mostrar nombres de superhéroes femeninos
    if genero == "F":
        superheroes_femeninos.append(superheroe)

    # c. Mostrar nombres de personajes masculinos
    if genero == "M":
        personajes_masculinos.append(nombre)

    # d. Determinar el superhéroe de Scott Lang
    if nombre.lower() == "scott lang":
        superheroe_scott_lang = superheroe

    # e. Mostrar datos de superhéroes o personajes que comienzan con 'S'
    if nombre.startswith("S") or superheroe.startswith("S"):
        coincidencias_s.append(p)

    # f. Determinar si Carol Danvers está en la cola e indicar su superhéroe
    if nombre.lower() == "carol danvers":
        carol_danvers_encontrada = True
        superheroe_carol = superheroe

    # Reencolar para conservar la cola intacta
    cola_mcu.arrive(p)


# --- Impresión de Resultados ---

print("\na. Nombre del personaje de Capitana Marvel:")
print(f"   - {personaje_capitana_marvel if personaje_capitana_marvel else 'No encontrado'}")

print("\nb. Nombres de superhéroes femeninos:")
for sh in superheroes_femeninos:
    print(f"   - {sh}")

print("\nc. Nombres de personajes masculinos:")
for pj in personajes_masculinos:
    print(f"   - {pj}")

print("\nd. Nombre del superhéroe de Scott Lang:")
print(f"   - {superheroe_scott_lang if superheroe_scott_lang else 'No encontrado'}")

print("\ne. Superhéroes o personajes que comienzan con la letra 'S':")
for p in coincidencias_s:
    print(f"   - Personaje: {p['nombre']} | Superhéroe: {p['superheroe']} | Género: {p['genero']}")

print("\nf. Búsqueda de Carol Danvers:")
if carol_danvers_encontrada:
    print(f"   - Carol Danvers se encuentra en la cola y su superhéroe es: {superheroe_carol}")
else:
    print("   - Carol Danvers no se encuentra en la cola.")
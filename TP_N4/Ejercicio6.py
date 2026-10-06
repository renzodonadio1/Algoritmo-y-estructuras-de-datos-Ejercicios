from list_ import List

# Lista de superhéroes de prueba (Marvel y DC)
superheroes_comics = [
    {"name": "Linterna Verde", "primera_aparicion": 1940, "casa": "DC", "short_bio": "Posee un anillo de poder con un traje icónico."},
    {"name": "Wolverine", "primera_aparicion": 1974, "casa": "Marvel", "short_bio": "Mutante con garras de adamantium y gran regeneración."},
    {"name": "Dr. Strange", "primera_aparicion": 1963, "casa": "DC", "short_bio": "Hechicero supremo protector de la realidad."},
    {"name": "Capitana Marvel", "primera_aparicion": 1967, "casa": "Marvel", "short_bio": "Héroe cósmica con traje de combate altamente poderoso."},
    {"name": "Mujer Maravilla", "primera_aparicion": 1941, "casa": "DC", "short_bio": "Princesa amazona equipada con su armadura de batalla."},
    {"name": "Flash", "primera_aparicion": 1940, "casa": "DC", "short_bio": "El hombre más rápido vivo con un traje escarlata."},
    {"name": "Star-Lord", "primera_aparicion": 1976, "casa": "Marvel", "short_bio": "Líder de los Guardianes de la Galaxia que porta una armadura especial."},
    {"name": "Batman", "primera_aparicion": 1939, "casa": "DC", "short_bio": "El caballero de la noche con armadura táctica."},
    {"name": "Superman", "primera_aparicion": 1938, "casa": "DC", "short_bio": "El último hijo de Krypton con superfuerza."}
]

# Instanciar la clase List y registrar el criterio de búsqueda por nombre
lista_heroes = List()
lista_heroes.add_criterion("name", lambda h: h["name"].lower())

for h in superheroes_comics:
    lista_heroes.append(h)

print("--- EJERCICIO 6 ---")

# a. Eliminar el nodo que contiene la información de Linterna Verde
print("\na. Eliminar a Linterna Verde:")
eliminado = lista_heroes.delete_value("linterna verde", "name")
if eliminado:
    print(f"   Se eliminó a: {eliminado['name']}")

# b. Mostrar el año de aparición de Wolverine
print("\nb. Año de aparición de Wolverine:")
pos_wolv = lista_heroes.search("wolverine", "name")
if pos_wolv is not None:
    print(f"   Wolverine apareció en el año {lista_heroes[pos_wolv]['primera_aparicion']}.")

# c. Cambiar la casa de Dr. Strange a Marvel
print("\nc. Cambiar la casa de Dr. Strange a Marvel:")
pos_doc = lista_heroes.search("dr. strange", "name")
if pos_doc is not None:
    lista_heroes[pos_doc]["casa"] = "Marvel"
    print(f"   Dr. Strange ahora pertenece a: {lista_heroes[pos_doc]['casa']}")

# d. Mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
print("\nd. Superhéroes con 'traje' o 'armadura' en su biografía:")
palabras_clave = ["traje", "armadura"]
for h in lista_heroes:
    bio = h["short_bio"].lower()
    if any(palabra in bio for palabra in palabras_clave):
        print(f"   - {h['name']}")

# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
print("\ne. Superhéroes con fecha de aparición anterior a 1963:")
for h in lista_heroes:
    if h["primera_aparicion"] < 1963:
        print(f"   - {h['name']} ({h['casa']}) - Año: {h['primera_aparicion']}")

# f. Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
print("\nf. Casa de Capitana Marvel y Mujer Maravilla:")
for nombre in ["capitana marvel", "mujer maravilla"]:
    pos = lista_heroes.search(nombre, "name")
    if pos is not None:
        print(f"   - {lista_heroes[pos]['name']}: {lista_heroes[pos]['casa']}")

# g. Mostrar toda la información de Flash y Star-Lord
print("\ng. Información completa de Flash y Star-Lord:")
for nombre in ["flash", "star-lord"]:
    pos = lista_heroes.search(nombre, "name")
    if pos is not None:
        print(f"   Info de {lista_heroes[pos]['name']}:")
        for clave, valor in lista_heroes[pos].items():
            print(f"     {clave}: {valor}")

# h. Listar los superhéroes que comienzan con la letra B, M y S
print("\nh. Superhéroes que comienzan con B, M y S:")
prefijos = ("B", "M", "S")
for h in lista_heroes:
    if h["name"].startswith(prefijos):
        print(f"   - {h['name']}")

# i. Determinar cuántos superhéroes hay de cada casa de comic
print("\ni. Cantidad de superhéroes por casa de cómic:")
conteo_casas = {}
for h in lista_heroes:
    casa = h["casa"]
    conteo_casas[casa] = conteo_casas.get(casa, 0) + 1

for casa, cantidad in conteo_casas.items():
    print(f"   - {casa}: {cantidad} superhéroe(s)")
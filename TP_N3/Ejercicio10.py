from queue import Queue
from stack import Stack

# Datos de prueba para cargar la cola de notificaciones
notificaciones = [
    {"hora": "10:15", "app": "Facebook", "mensaje": "Tienes una solicitud de amistad"},
    {"hora": "11:45", "app": "Twitter", "mensaje": "Aprendiendo Python en la universidad"},
    {"hora": "12:30", "app": "Instagram", "mensaje": "A alguien le gustó tu foto"},
    {"hora": "14:10", "app": "Twitter", "mensaje": "Curso de JavaScript y HTML"},
    {"hora": "15:20", "app": "Facebook", "mensaje": "Nuevo evento cerca de ti"},
    {"hora": "15:50", "app": "Twitter", "mensaje": "Librerías de Python para datos"},
    {"hora": "16:05", "app": "WhatsApp", "mensaje": "Mensaje de grupo"}
]

# Cargar la cola principal
cola_notificaciones = Queue()
for n in notificaciones:
    cola_notificaciones.arrive(n)


print("EJERCICIO 10: NOTIFICACIONES DE SMARTPHONE")


# a. Eliminar de la cola todas las notificaciones de Facebook
def eliminar_facebook(cola):
    tamanio_original = cola.size()
    for _ in range(tamanio_original):
        notificacion = cola.attention()
        if notificacion["app"].lower() != "facebook":
            cola.arrive(notificacion)

print("\na. Eliminando notificaciones de Facebook...")
eliminar_facebook(cola_notificaciones)


# b. Mostrar notificaciones de Twitter que incluyan 'Python' (no destructivo)
def mostrar_twitter_python(cola):
    print("   Notificaciones de Twitter sobre Python:")
    for _ in range(cola.size()):
        notificacion = cola.attention()
        if notificacion["app"].lower() == "twitter" and "python" in notificacion["mensaje"].lower():
            print(f"     [{notificacion['hora']}] {notificacion['app']}: {notificacion['mensaje']}")
        cola.arrive(notificacion)

print("\nb. Filtrando notificaciones de Twitter:")
mostrar_twitter_python(cola_notificaciones)


# c. Almacenar en una pila las notificaciones entre las 11:43 y las 15:57 y contarlas
def filtrar_por_horario(cola):
    pila_temporal = Stack()
    hora_inicio = "11:43"
    hora_fin = "15:57"
    
    for _ in range(cola.size()):
        notificacion = cola.attention()
        if hora_inicio <= notificacion["hora"] <= hora_fin:
            pila_temporal.push(notificacion)
        cola.arrive(notificacion)
        
    return pila_temporal

pila_horario = filtrar_por_horario(cola_notificaciones)

print(f"\nc. Cantidad de notificaciones entre las 11:43 y las 15:57: {pila_horario.size()}")
print("   Notificaciones guardadas en la pila temporal:")
pila_aux = Stack()
while pila_horario.size() > 0:
    n = pila_horario.pop()
    print(f"     [{n['hora']}] {n['app']}: {n['mensaje']}")
    pila_aux.push(n)

# Restaurar la pila
while pila_aux.size() > 0:
    pila_horario.push(pila_aux.pop())
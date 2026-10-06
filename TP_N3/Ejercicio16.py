from priority_queue import PriorityQueue  # O la clase ColaPrioridad de tu cátedra

# Instanciar la cola de prioridad
cola_impresion = PriorityQueue()

# Definición de prioridades
PRIORIDAD_EMPLEADO = 1
PRIORIDAD_TI = 2
PRIORIDAD_GERENTE = 3


print("--- EJERCICIO 16: COLA DE IMPRESIÓN CON PRIORIDAD ---")

# a. Cargar tres documentos de empleados
print("\na. Cargando 3 documentos de empleados...")
cola_impresion.arrive("Doc_Empleado_1", PRIORIDAD_EMPLEADO)
cola_impresion.arrive("Doc_Empleado_2", PRIORIDAD_EMPLEADO)
cola_impresion.arrive("Doc_Empleado_3", PRIORIDAD_EMPLEADO)


# b. Imprimir el primer documento de la cola
print("\nb. Imprimiendo el primer documento de la cola:")
if cola_impresion.size() > 0:
    doc = cola_impresion.attention()
    print(f"   Imprimiendo: {doc}")


# c. Cargar dos documentos del staff de TI
print("\nc. Cargando 2 documentos del staff de TI...")
cola_impresion.arrive("Doc_TI_1", PRIORIDAD_TI)
cola_impresion.arrive("Doc_TI_2", PRIORIDAD_TI)


# d. Cargar un documento del gerente
print("\nd. Cargando 1 documento del gerente...")
cola_impresion.arrive("Doc_Gerente_1", PRIORIDAD_GERENTE)


# e. Imprimir los dos primeros documentos de la cola
print("\ne. Imprimiendo los dos primeros documentos de la cola:")
for i in range(2):
    if cola_impresion.size() > 0:
        doc = cola_impresion.attention()
        print(f"   Imprimiendo [{i + 1}]: {doc}")


# f. Cargar dos documentos de empleados y uno de gerente
print("\nf. Cargando 2 documentos de empleados y 1 de gerente...")
cola_impresion.arrive("Doc_Empleado_4", PRIORIDAD_EMPLEADO)
cola_impresion.arrive("Doc_Empleado_5", PRIORIDAD_EMPLEADO)
cola_impresion.arrive("Doc_Gerente_2", PRIORIDAD_GERENTE)


# g. Imprimir todos los documentos restantes de la cola de impresión
print("\ng. Imprimiendo todos los documentos restantes en orden de prioridad:")
while cola_impresion.size() > 0:
    doc = cola_impresion.attention()
    print(f"   Imprimiendo: {doc}")
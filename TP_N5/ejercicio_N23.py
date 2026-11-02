from nodoArbol import nodoArbol

def por_nivel(raiz):
    """Recorre e imprime el árbol nivel por nivel de izquierda a derecha."""
    if raiz is None:
        return
    
    cola = []
    # Arribo a la cola (enqueue)
    cola.append(raiz)
    
    while len(cola) > 0:
        # Atención de la cola (dequeue)
        nodo = cola.pop(0)
        print(f"Dato: {nodo.info}")
        
        # Si tiene hijo izquierdo, lo agregamos a la cola
        if nodo.izq is not None:
            cola.append(nodo.izq)
            
        # Si tiene hijo derecho, lo agregamos a la cola
        if nodo.der is not None:
            cola.append(nodo.der)

# --- Ejemplo de uso ---
if __name__ == "__main__":
    raiz = nodoArbol()
    raiz.info = 10
    
    raiz.izq = nodoArbol()
    raiz.izq.info = 5
    
    raiz.der = nodoArbol()
    raiz.der.info = 20
    
    raiz.izq.izq = nodoArbol()
    raiz.izq.izq.info = 2
    
    print("Recorrido por nivel:")
    por_nivel(raiz)
from nodoArbol import nodoArbol

def altura(raiz):
    """Calcula la altura de un árbol binario de manera recursiva."""
    if raiz is None:
        return -1  # Retorna -1 si está vacío, o 0 si consideras un solo nodo como altura 0
    else:
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        return 1 + max(alt_izq, alt_der)

def contar_hojas(raiz):
    """Cuenta la cantidad de nodos hoja en el árbol."""
    if raiz is None:
        return 0
    if raiz.izq is None and raiz.der is None:
        return 1
    return contar_hojas(raiz.izq) + contar_hojas(raiz.der)

# Ejemplo
if __name__ == "__main__":
    raiz = nodoArbol()
    raiz.info = 10
    
    raiz.izq = nodoArbol()
    raiz.izq.info = 5
    
    raiz.der = nodoArbol()
    raiz.der.info = 20
    
    print(f"Altura del árbol: {altura(raiz)}")
    print(f"Cantidad de hojas: {contar_hojas(raiz)}")
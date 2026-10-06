# priority_queue.py
import heapq

class PriorityQueue:
    """
    TDA Cola de Prioridad.
    Permite insertar elementos con una prioridad asociada.
    Atiende primero los elementos de MAYOR valor de prioridad.
    """

    def __init__(self):
        self._elements = []
        self._index = 0  # Desempata el orden de llegada a igual prioridad

    def arrive(self, value, priority: int) -> None:
        """Agrega un elemento a la cola con su prioridad."""
        # Se usa -priority porque heapq implementa un Min-Heap por defecto
        heapq.heappush(self._elements, (-priority, self._index, value))
        self._index += 1

    def attention(self):
        """Atiende (elimina y devuelve) el elemento con mayor prioridad."""
        if self.size() > 0:
            return heapq.heappop(self._elements)[2]
        return None

    def size(self) -> int:
        """Devuelve la cantidad de elementos en la cola."""
        return len(self._elements)

    def is_empty(self) -> bool:
        """Verifica si la cola está vacía."""
        return len(self._elements) == 0
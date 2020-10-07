from errors.empty import Empty

class ArrayQueue:

  """Implementação de uma fila (LIFO) usando uma lista do Python."""
  DEFAULT_CAPACITY = 10               # capacidade das novas filas

  def __init__(self):
    """Cria uma fila vazia."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Retorna o número de elementos da fila."""
    return len(self._data)

  def is_empty(self):
    """Retorna True se a fila estiver vazia."""
    return self._size == 0

  def first(self):
    """Retorna mas não remove, o elemento na frente da fila.
    Dispara uma exceção Empty se a fila estiver vazia.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove e retorna o primeiro elemento da fila. (LIFO)
    Dispara uma exceção Empty se a fila estiver vazia.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None    # Ajuda o garbage colector do Python
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer
  
  def enqueue(self, e):
    """Adiciona um elemento no fim da fila.
    """
    if self._size == len(self._data):
      self._resize(2 * len(self._data)) # dobra o tamanho do array
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1
  
  def _resize(self, cap):
    """Altera o tamanho do array para uma nova capacidade."""
    old = self._data        # mantem uma referencia da ultima fila
    self._data = [None] * cap             # aloca uma nova lista
    walk = self._front
    for k in range(self._size):           # considera somente os elementos existentes
      self._data[k] = old[walk]           # dá um shift nos indices
      walk += (1 + walk) % len(old)       # usa o módulo da ultima fila
    self._front = 0         # frente foi reavaliada
    
    

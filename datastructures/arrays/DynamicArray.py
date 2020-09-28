import ctypes

class DynamicArray:
  """Classe de array dinâmico semelhante as listas nativas do Python."""
  def __init__(self):
    """Cria um array vazio."""
    self._n = 0                                   # número atual de elementos
    self._capacity = 1                            # capacidade padrão do array
    self._A = self._make_array(self._capacity)    # array de baixo nível

  def __len__(self):
    """Retorna o número de elementos armazenados no array."""
    return self._n

  def __getitem__(self, k):
    """Retorna o elemento no índice k."""
    if not 0 <= k < self._n:
      raise IndexError('invalid index')
    return self._A[k]                             # retorna o elemento do array
  
  def append(self, obj):
    """Adiciona um elemento no fim do array."""
    if self._n == self._capacity:                 # sem mais espaço no array
      self._resize(2 * self._capacity)            # então dobramos a capacidade
    self._A[self._n] = obj
    self._n += 1

  def insert(self, k, obj):
    """Insere um elemento no índice k, deslocando todos os elementos
    subsequentes."""
    if self._n == self._capacity:                 # sem mais espaço no array
      self._resize(2 * self._capacity)            # então dobramos a capacidade
    for j in range(self._n, k, -1):               # desloca os elementos de forma decrescente
      self._A[j] = self._A[j - 1]
    self._A[k] = obj                              # armazena o novo elemento
    self._n += 1

  def remove(self, obj):
    """Remove a primeira ocorrência do objeto (ou dispara um ValueError)."""
    for k in range(self._n):
      if self._A[k] == obj:                     # encontrou o elemento
        for j in range(k, self._n - 1):           # desloca os outros elementos do array
          self._A[j] = self._A[j + 1]
        self._A[self._n - 1] = None               # ajuda o Garbage Collector do Python
        self._n -= 1                              # agora temos -1 item
        return                                    # quebra a execução do método
    raise ValueError('value not found')           # somente é chamado caso não encontre o obj
  
  def _resize(self, c):                           # sem utilidade pública
    """Modifica a capacidade interna do array."""
    B = self._make_array(c)
    for k in range(self._n):
      B[k] = self._A[k]
    self._A = B
    self._capacity = c

  def _make_array(self, c):                       # sem utilidade pública
    """Retorna um novo array com capacidade c."""
    return (c * ctypes.py_object)()

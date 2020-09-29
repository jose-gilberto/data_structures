from datastructures.errors.empty import Empty

class ArrayStack:
  """implementação de uma pilha LIFO usando a classe de listas do Python."""
  def __init__(self):
    """Cria uma nova pilha vazia."""
    self._data = []                             # instância não pública

  def __len__(self):
    """Retorna o número de elementos na pilha."""
    return len(self._data)

  def is_empty(self):
    """Retorna true se a pilha estiver vazia."""
    return len(self._data) == 0

  def push(self, e):
    """Adiciona um novo elemento no topo da pilha."""
    self._data.append(e)                        # novo item armazenado no topo da pilha

  def top(self):
    """Retorna (mas não remove) o elemento no topo da pilha.
    
    Dispara uma Empty Exception caso a pilha esteja vazia.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data[-1]                       # retorna o último item da lista

  def pop(self):
    """Remove o elemento do topo da pilha e retorna ele. (LIFO)
    
    Dispara uma Empty Exception caso a pilha esteja vazia.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data.pop()                     # remove o último item da lista

def insertion_sort(A):
  """Ordena uma lista de elementos comparáveis em uma ordem decrescente."""
  for k in range(1, len(A)):          # vai de 1 até n-1
    cur = A[k]                        # elemento atual a ser manipulado
    j = k                             # encontra o índice correto (j) para o atual
    while j > 0 and A[j-1] > cur:     # elemento A[j-1] deve estar depois do atual
      A[j] = A[j-1]
      j -= 1
    A[j] = cur                        # o elemento atual agora está no lugar correto

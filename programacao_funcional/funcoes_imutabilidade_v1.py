from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

# Não muda o conteúdo
print(sorted(valores))
print(valores)
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(list(reversed(valores)))
print(valores)

# Muda o conteúdo
# valores.sort()
# print(valores)
# valores.reverse()
# print(valores)

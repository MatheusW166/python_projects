from functools import reduce
from operator import add

# Tupla não é mutável.
valores = (30, 10, 25, 70, 100, 94)

print(tuple(sorted(valores)))
print(valores)
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(tuple(reversed(valores)))
print(valores)

# Gera erro
# valores.sort()
# print(valores)
# valores.reverse()
# print(valores)

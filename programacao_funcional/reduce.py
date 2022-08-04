from functools import reduce


pessoas = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26},
    {'nome': 'Arthur', 'idade': 15},
    {'nome': 'Rebeca', 'idade': 10},
    {'nome': 'Tiago', 'idade': 18},
    {'nome': 'Gabriel', 'idade': 21},
    {'nome': 'Mariana', 'idade': 6},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)

soma_idades = reduce(lambda idades, p: idades + p['idade'], menores, 0)
print(soma_idades)

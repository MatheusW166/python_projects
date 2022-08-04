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
print(list(menores))

nomes_grandes = filter(lambda p: len(p['nome']) > 6, pessoas)
print(list(nomes_grandes))

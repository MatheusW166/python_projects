pessoas = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26},
]

frases = list(map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', pessoas,))
print(frases)

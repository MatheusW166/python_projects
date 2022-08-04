pessoa = {'nome': 'Matheus', 'idade': 22}

# Valor default
print(pessoa.get('altura', -1))
print(pessoa)

pessoa.update({'altura': 1.70, 'idade': 23})
print(pessoa)

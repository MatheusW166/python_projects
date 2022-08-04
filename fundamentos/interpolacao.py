from string import Template


nome, idade = 'Ana', 30
print('Nome: %s Idade: %.2f'%(nome, idade)) # Antigo
print('Nome: {0} Idade: {1}'.format(nome, idade))
print(f'Nome: {nome} Idade: {idade}') # Recomendado

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))

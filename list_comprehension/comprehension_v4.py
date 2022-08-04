# Gera com base no uso.
generator = (i**2 for i in range(1, 11) if i % 2 == 0)

for numero in generator:
    print(numero)

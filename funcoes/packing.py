def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


# numeros é uma tupla com os parâmetros.
def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


# Packing
print(soma_n(1, 1, 1, 1, 1, 1, 1))

# Unpacking
lista = [1, 1, 1, 1, 1, 1, 1]
print(soma_n(*lista))

def mapear(funcao, iterator):
    return (funcao(elemento) for elemento in iterator)


if __name__ == '__main__':
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))

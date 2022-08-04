def mapear(funcao, iterator):
    it = iter(iterator)
    elemento = next(it, None)
    if elemento == None:
        return tuple()
    return (funcao(elemento),) + mapear(funcao, it)


def mapear2(funcao, iterator):
    for elemento in iterator:
        print('Passando por aqui.')
        yield funcao(elemento)


if __name__ == '__main__':
    print(list(mapear2(lambda x: x ** 2, [2, 3, 4])))

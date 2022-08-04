# Forma de função, cria um generator
def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'índigo'
    yield 'violeta'


# Forma de comprehension
generator_conprehension = (cor for cor in ('vermelho',
                                           'laranja',
                                           'amarelo',
                                           'verde',
                                           'azul',
                                           'índigo',
                                           'violeta',))


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    print(type(generator_conprehension))
    while True:
        print(next(generator))

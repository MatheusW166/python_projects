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

    for cor in cores_arco_iris():
        print(cor)
    print('Fim!')

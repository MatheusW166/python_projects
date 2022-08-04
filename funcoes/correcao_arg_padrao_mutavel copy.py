def fibonacci_correcao_1(sequencia=None):
    # Utilizando None.
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


def fibonacci_correcao_2(sequencia=[0, 1]):
    # Sem mexer na lista.
    return sequencia + [sequencia[-1] + sequencia[-2]]


def fibonacci_correcao_3(sequencia=(0, 1)):
    # Utilizando tuplas.
    return list(sequencia + (sequencia[-1] + sequencia[-2],))


def fibonacci_correcao_4(sequencia=[0, 1]):
    # Criando outro objeto.
    nova_sequencia = sequencia + [sequencia[-1] + sequencia[-2]]
    return nova_sequencia


# O endereço de memória do parâmetro permanece o mesmo.
if __name__ == '__main__':
    inicio = fibonacci_correcao_1()
    print(inicio, id(inicio))
    print(fibonacci_correcao_1(inicio))
    restart = fibonacci_correcao_1()
    print(restart, id(restart))
    assert restart == [0, 1, 1]

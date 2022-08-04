def get_tipo_dia_generator(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana',
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** dia inválido **')


def get_tipo_dia_lista(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana',
    }
    dia_escolhido = [tipo for numeros, tipo in dias.items() if dia in numeros]
    return dia_escolhido[0] if len(dia_escolhido) > 0 else '** inválido **'


for i in range(0, 9):
    print(f'{i}: {get_tipo_dia_generator(i)}')

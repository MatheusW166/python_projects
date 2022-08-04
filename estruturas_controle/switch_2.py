def get_tipo_dia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia da semana',
        3: 'Dia da semana',
        4: 'Dia da semana',
        5: 'Dia da semana',
        6: 'Dia da semana',
        7: 'Fim de semana',
    }
    return dias.get(dia, 'inválido')


for dia in range(8):
    print(get_tipo_dia(dia))

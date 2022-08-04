# **kwargs

# **podium é um dict com os parâmetros.
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    podium = {
        'primeiro': 'L. Hamilton',
        'segundo': 'M. Verstappen',
        'terceiro': 'S. Vettel',
    }
    resultado_f1(**podium)
    print('=========================')
    resultado_f1(**{
        'terceiro': 'L. Hamilton',
        'primeiro': 'M. Verstappen',
        'segundo': 'S. Vettel',
    })

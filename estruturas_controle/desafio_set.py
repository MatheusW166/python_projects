PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = ['João gosta de futebol e política', 'A praia foi divertida', ]

# Se finaliza o laço, vai para o else
for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas.', intersecao)
    else:
        print('Texto autorizado.', texto)

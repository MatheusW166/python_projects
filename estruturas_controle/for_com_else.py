PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = ['João gosta de futebol e política', 'A praia foi divertida', ]

# Se finaliza o laço, vai para o else
for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Há palavras proibidas.')
            break
    else:
        print('Texto autorizado:', texto)

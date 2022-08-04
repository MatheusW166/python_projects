def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista_txt = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista_txt}</ul>'


if __name__ == '__main__':
    # Necessário usar nomeados após packing parametros
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))

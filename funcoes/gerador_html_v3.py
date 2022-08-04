def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista_txt = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista_txt}</ul>'


if __name__ == '__main__':
    print(tag_bloco(classe='lista', conteudo=tag_lista('Matheus', 'João')))

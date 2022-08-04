bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def get_params(suportados, atributos):
    return ' '.join(
        f'{attr.split("_")[-1]}="{value}"' for attr, value in atributos.items()
        if attr in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **atributos):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **atributos)
    return f'<{tag} {get_params(bloco_atrs, atributos)} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **atributos):
    lista_txt = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {get_params(ul_atrs, atributos)}>{lista_txt}</ul>'


if __name__ == '__main__':
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
          bloco_accesskey='m', bloco_id='conteudo', ul_id='lista',))

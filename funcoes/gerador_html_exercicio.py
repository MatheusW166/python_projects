import re


def get_attrs(**kwargs):
    tipo_finder = re.compile(r'\w+?\_')
    return ' '.join(f'{tipo_finder.sub("", key, count=1)}="{value}"' for key,
                    value in kwargs.items())


def tag(tag, *args, **kwargs):
    content = ''.join(args)
    attrs = get_attrs(**kwargs)
    return f'<{tag} {attrs}>{content}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Exemplo doido, por'),
            tag('strong', 'Professor 1', id='p1'),
            tag('span', '.'),
            html_id='paragrafo',
            html_class='alert',
            html_destaque_aqui=True,
            html_ok=False
            )
    )

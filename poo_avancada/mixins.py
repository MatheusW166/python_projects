'''
    Na herança, a prioridade para invocação é da esquerda pra direita.
    O super() busca em todas as classes incluídas na herança.
'''


class HtmlToStringMixin:
    def __str__(self):
        super().teste()
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def teste(self):
        print('Executando teste.')


class PessoaHtml(HtmlToStringMixin, Pessoa):
    pass


p1 = Pessoa('Joao')
print(p1)

p2 = PessoaHtml('João')
print(p2)

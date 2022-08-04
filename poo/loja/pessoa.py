MAIOR_IDADE = 18


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Pessoa(nome="{self.nome}", idade="{self.idade}")'

    def is_adult(self):
        return self.idade >= MAIOR_IDADE

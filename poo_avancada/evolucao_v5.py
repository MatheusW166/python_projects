'''
    Uma alternativa para classes abstratas em Python.
'''


class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    # Método "abstrato"
    @property
    def inteligente(self):
        raise NotImplementedError('Propriedade não implementada.')

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade <= 0:
            raise ValueError('Idade deve ser positivo!')
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Nearderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Nearderthalensis', 'Sapiens',)
        return ('Australopiteco',) + tuple(f'{adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        print(f'<{cls.__name__}>')
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    jose.idade = 40
    print(f'Nome: {jose.nome} Idade: {jose.idade}')

    try:
        print(jose.inteligente)
    except NotImplementedError:
        print('Propriedade abstrata.')

    goku = Neanderthal('Goku')
    goku.idade = 32
    print(f'Nome: {goku.nome} Idade: {goku.idade}')
    print(goku.inteligente)

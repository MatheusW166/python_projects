'''
    Outra alternativa para classes abstratas em Python.
'''

from abc import ABCMeta, abstractmethod


class Humano(metaclass=ABCMeta):
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    # Método "abstrato"
    @property
    @abstractmethod
    def inteligente(self):
        pass

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

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    humano = Humano('Matheus')  # Erro, impossível instanciar classe abstrata

    jose = HomoSapiens('José')
    jose.idade = 40
    print(f'Nome: {jose.nome} Idade: {jose.idade}')
    print(jose.inteligente)

    goku = Neanderthal('Goku')
    goku.idade = 32
    print(f'Nome: {goku.nome} Idade: {goku.idade}')
    print(goku.inteligente)

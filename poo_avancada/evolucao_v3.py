class Humano:
    # Atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
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


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    jose.set_idade(40)
    print(f'Nome: {jose.nome} Idade: {jose.get_idade()}')

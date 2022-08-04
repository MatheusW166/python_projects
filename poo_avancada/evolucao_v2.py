'''
    Método de classe -> Recebe a classe como parâmetro.
    Método estático -> Não recebe self, mas é acessível pela instância também.
'''


class Humano:
    # Atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

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
    grokn = Neanderthal('grokn')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(
        f'Evolução (a partir da instância :O): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluído? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluído? {Neanderthal.is_evoluido()}')
    print(f'jose evoluído? {jose.is_evoluido()}')
    print(f'grokn evoluído? {grokn.is_evoluido()}')

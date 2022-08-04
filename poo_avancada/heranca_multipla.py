class Animal:
    @property
    def capacidades(self):
        print('< Animal >')
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        print('< Homem >')
        # super() pode não ser Animal, e sim a classe que foi herdada jutno na herança múltipla.
        return super().capacidades + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidades(self):
        print('< Aranha >')
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class SpiderMan(Homem, Aranha):
    @property
    def capacidades(self):
        print('< SpiderMan >')
        return super().capacidades + \
            ('bater em bandidos', 'atirar entre prédios')


if __name__ == '__main__':

    peter = SpiderMan()
    print(f'Homem Aranha: {peter.capacidades}')

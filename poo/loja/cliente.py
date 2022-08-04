from .pessoa import Pessoa
from functools import reduce


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        compras = self.compras
        if len(compras) == 0:
            return None
        return sorted(compras, key=lambda e: e.data)[-1].data

    def total_compras(self):
        return reduce(lambda a, b: a.valor + b.valor, self.compras)

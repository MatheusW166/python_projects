from .cliente import Cliente
from .vendedor import Vendedor
from .compra import Compra


waz = 'Variável também deve estar no __all__'


def bar():
    return 'Função precisa estar no __all__'


__all__ = ['Cliente', 'Compra', 'Vendedor', 'bar', 'waz']

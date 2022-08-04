'''
    Este arquivo exemplifica um padrão de projeto chamado "facade".
    O pacote serve como fachada que exibe funcionalidades de outros pacotes ou módulos.
    Imports não precisam necessariamente estar no __all__, mas são colocados por convenção.
'''

from pacote1.modulo1 import soma
from pacote2.modulo1 import sub

__all__ = ['soma', 'sub']

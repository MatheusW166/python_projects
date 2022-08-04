#! python
from sys import argv
from math import pi


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print("É necessário informar o raio do círculo.")
    print(f"Sintaxe: {argv[0]} <raio>")
    exit(1)


def circulo(r):
    return pi * float(r) ** 2


if __name__ == '__main__':
    if len(argv) < 2:
        help()
    if not argv[1].isnumeric():
        print(TerminalColor.ERRO +
              'O raio deve ser numérico' +
              TerminalColor.NORMAL)
        help()

    r = argv[1]
    area = circulo(r)
    print(area)

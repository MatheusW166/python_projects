#! python
from ast import arg
from math import pi
from sys import argv


def help():
    print("É necessário informar o raio do círculo.")
    print(f"Sintaxe: {argv[0]} <raio>")


def circulo(r):
    return pi * float(r) ** 2


if __name__ == '__main__':
    if len(argv) < 2:
        help()
        exit(1)
    if not argv[1].isnumeric():
        help()
        print('O raio deve ser numérico')
        exit(1)

    r = argv[1]
    area = circulo(r)
    print(area)

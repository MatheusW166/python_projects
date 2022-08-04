#! python
from math import pi


def circulo(r):
    print('Área do círculo:', pi * r ** 2)


if __name__ == '__main__':
    r = float(input('Informe o raio: '))
    circulo(r)

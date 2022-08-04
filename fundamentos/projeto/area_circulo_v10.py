#! python
from math import pi
import sys


def circulo(r):
    return pi * float(r) ** 2


if __name__ == '__main__':
    r = sys.argv[1]
    area = circulo(r)
    print(area)

# Gerador infinito de números
def sequence():
    num = 0
    while True:
        yield num
        num += 1


def fibonacci():
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        yield b


if __name__ == '__main__':

    seq = sequence()
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))

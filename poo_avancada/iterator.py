class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    # Para iterar a partir do for (objeto iterável)
    def __iter__(self):
        print('Retornando objeto iterável...')
        return self

    # Para iterar a partir do for (iterator)
    def __next__(self):
        print('Iterando...')
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    print('==================')

    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

    print('==================')
    for cor in RGB():
        print(cor)

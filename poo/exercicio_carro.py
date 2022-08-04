class Carro:
    def __init__(self, maxima):
        self.maxima = maxima
        self.atual = 0

    def acelerar(self, delta=5):
        nova = self.atual + delta
        self.atual = nova if nova < self.maxima else self.maxima

    def frear(self, delta=5):
        nova = self.atual - delta
        self.atual = nova if nova > 0 else 0

    def __str__(self):
        return f'Carro(maxima={self.maxima}, atual={self.atual})'


if __name__ == '__main__':
    c1 = Carro(220)
    c1.acelerar(50)

    c1.frear(1)
    c1.frear(100)

    print(c1)

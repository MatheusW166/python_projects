class Data:
    def __init__(self, dia='01', mes='01', ano='1970'):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data('26', '07', '2022')
print(d1)

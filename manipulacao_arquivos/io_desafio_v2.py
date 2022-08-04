from urllib import request
import csv

URL = r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv'


def read(url):
    with request.urlopen(url) as input:
        dados = input.read().decode('ISO-8859-1')
        registros = [f'{row[8]}: {row[3]}'
                     for row in csv.reader(dados.splitlines())]
    return registros


if __name__ == '__main__':
    resposta = read(URL)
    print(resposta[:5])

import csv

PATH = 'desafio-ibge.csv'

with open(PATH, encoding='ISO-8859-1') as file:
    data = [(row[3], row[8]) for row in csv.reader(file)]

print(data[:5])

from functools import reduce
from locale import setlocale, LC_ALL
from calendar import mdays, month_name

# Pt-Br
setlocale(LC_ALL, 'pt_BR')

meses_31 = filter(lambda nMes: mdays[nMes] == 31, range(1, 13))
nomes_meses = map(lambda nMes: month_name[nMes], meses_31)
texto_meses_31 = reduce(
    lambda txt, mes:  txt + f'- {mes}\n', nomes_meses, 'Meses com 31 dias:\n')
print(texto_meses_31)

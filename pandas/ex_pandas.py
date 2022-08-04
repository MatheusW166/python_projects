from numpy import NaN
import pandas as pd

# usecols=['ordem_ano', 'dia'])
df = pd.read_csv('Operacoes_Especiais.csv', encoding='ISO-8859-1', sep=';')
print(df.shape)  # rows X columns
print(df.size)  # rows.columns = size
# print(df[['nome_op', 'ordem_ano']].head())

'''
NOVA COLUNA
'''
# df['nova_coluna'] = 'new_' + df['nome_op']
# print(df.head())
# print(df[df.dia < 10].head())

'''
SELEÇÃO
'''
# print(df.loc[0:6])  # linha, colunas
# print(df.loc[[1, 3, 4]])
# print(df.loc[4:6, ['nome_op', 'dia']])
# print(df.loc[4:6, 'ordem_ano':'nome_op'])
# print(df.iloc[:5, 3:5])
# print(df.loc[df.dia < 10].head())


'''
ORDENAÇÃO
'''
# df.sort_values(['ano', 'mes', 'dia'], ascending=False, inplace=True)
# print(df.head())


'''
VETORES LÓGICOS SÃO RETORNADOS
'''
# print((df.mes < 6).head())
# print(df[df.mes < 6].head())


'''
SELEÇÃO COM E e OU
'''
# print(df.loc[(df.mes < 6) & (df.dia > 10), ['nome_op', 'mes', 'dia', ]].head())


'''
GROUP BY
'''
df.replace(NaN, 0, inplace=True)
# print(df.loc[df.mun == 'SP', 'm_p_prevent':].head())
# print(df.loc[:, ['mun', 'm_p_prevent']].groupby(['mun']).mean())
print(df.loc[:, ['mun', 'uf', 'm_p_prevent']].groupby(['uf', 'mun']).mean())

'''
DICT PARA CSV
'''
dft = pd.DataFrame.from_dict(
    {'col1': ['val1', 'val2'], 'col2': ['val3', 'val4']})
dft.to_csv('dict_to_csv.csv')

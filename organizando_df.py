import pandas as pd

data = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]

list('321') # ['3', '2', '1']

df = pd.DataFrame(data, list('321'), list('ZYX'))

df.sort_index(inplace=True)   # organiza pelo índice das linhas
df.sort_index(inplace=True,axis=1)   # organiza pelo índice das colunas

df.sort_values(by=['X', 'Y'], inplace=True) # ordenar por uma coluna específica, aceita tanto um str quanto um list de str
df.sort_values(by='3', inplace=True, axis=1) # ordenar por uma linha específica


data2 = [
	[9, 6, 3],
	[8, 5, 2],
	[7, 4, 1]
]

df2 = pd.DataFrame(data2, list('ZYX'), list('CBA'))
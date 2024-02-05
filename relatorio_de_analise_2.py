import pandas as pd 

dados = pd.read_csv('aluguel.csv', sep = ';')
dados.head(10)

tipo_de_imovel = dados['Tipo']
type(tipo_de_imovel)       # pandas.core.series.Series
tipo_de_imovel.drop_duplicates(inplace = True) # inplace = True modifica a variável com a execução do método

tipo_de_imovel

## Organizando visualização
tipo_de_imovel = pd.DataFrame(tipo_de_imovel)

# modificando o index
tipo_de_imovel.index    # exibe os indexes atuais
tipo_de_imovel.shape[0]    # o tamanho do dataframe = 22

tipo_de_imovel.index = range(tipo_de_imovel.shape[0])
tipo_de_imovel.columns.name = 'Id'

# Series
data = [1,2,3,4,5]
s = pd.Series(data)
s

index = ['Linha' + str(i) for i in range(5)]
index

s = pd.Series(data = data, index = index)
s

s1 = s + 2

# DataFrame
data = [
   [1, 2, 3], 
   [4, 5, 6],
   [7, 8, 9]
]

df1 = pd.DataFrame(data = data)

index = ['Linha' + str(i) for i in range(3)]
columns = ['Coluna' + str(i) for i in range(3)]

df1 = pd.DataFrame(data = data, index = index, columns = columns)

data = {
   'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
   'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
   'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}
}

df2 = pd.DataFrame(data)

df1[ df1 > 0] = 'A'
df1
df2[ df2 > 0] = 'B'
df2
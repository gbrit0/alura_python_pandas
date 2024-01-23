import pandas as pd 

dados = pd.read_csv('aluguel.csv', sep = ';')
dados.head(10)

tipo_de_imovel = dados['Tipo']
type(tipo_de_imovel)       # pandas.core.series.Series
tipo_de_imovel.drop_duplicates(inplace = True)

tipo_de_imovel
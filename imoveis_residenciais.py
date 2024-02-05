import pandas as pd
dados = pd.read_csv('aluguel.csv', sep=';')

list(dados['Tipo'].drop_duplicates())

residencial = [
   'Quitinete',
   'Casa',
   'Apartamento',
   'Casa de Condomínio',
   'Casa de Vila'
]

selecao = dados['Tipo'].isin(residencial) # isin(residencial) retorna bool se está dentro da lista em residencial

dados_residencial = dados[selecao] # a partir da seleção, copia  o dataframe quando for true

list(dados_residencial['Tipo'].drop_duplicates())     # verificação se a lista gerada é compátível com residencial

dados_residencial.shape[0]    # 22580
dados.shape[0]                # 32960

dados_residencial.index = range(len(dados_residencial)) # redefinição do index

# Exportando a Base de Dados

dados_residencial.to_csv('aluguel_residencial.csv', sep=';')   # deste modo, exporta o índice como uma coluna. 
                                                               # ao usar o read_csv, a coluna de índice vai aparecer desnescessariamente
dados_residencial.to_csv('aluguel_residencial.csv', sep=';', index=False)

dados_residencial_2 = pd.read_csv('aluguel_residencial.csv', sep=';')
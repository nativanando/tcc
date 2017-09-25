import pandas as pd
series = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/microsoft_normalizado.txt',header=0)

series['open-normalizado-teste'] = series['Open']
open_normalizado = []
close_normalizado = []
low_nom
for i in range(series.__len__()):
    resultado.append((series.iloc[i]['Open'] - min(series['Open'])) / (max(series['Open']) - min(series['Open'])))

series['open-normalizado-teste'] = resultado
print (series)

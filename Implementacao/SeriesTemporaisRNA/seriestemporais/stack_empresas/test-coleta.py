import pandas as pd
series = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/amazon_normalizado.txt',header=0)

print (max(series['Open']))

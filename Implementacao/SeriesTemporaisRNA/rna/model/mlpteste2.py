import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/resultado_series/microsoft_predicao_200.txt',header=0)
i = 0;
dataset['Variation'] = dataset['Abertura'].sub(dataset['Predição'])
print (dataset)
print(dataset.describe())

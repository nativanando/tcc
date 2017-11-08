import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/resultado_series/'
                    'amazon_predicao_200.txt', header=0)


dados['Data'] = pd.to_datetime(dados['Data'], format="%d-%m-%Y")
linha = dados['Data']
coluna = dados['Abertura']
coluna1 = dados['Predição']
fig, ax = plt.subplots()
ax.plot(linha, coluna, 'go')  # green bolinha
ax.plot(linha, coluna1, 'ro')  # green bolinha
fig.set_size_inches(12, 8, forward=True)
plt.legend(['Valor de abertura', 'Predição'])
ax.plot(linha, coluna, 'k:', color='orange')  # linha pontilha orange
ax.plot(linha, coluna1, 'k:', color='blue')  # linha pontilha orange
plt.grid(True)
plt.show()
plt.close()
print (dados.describe())
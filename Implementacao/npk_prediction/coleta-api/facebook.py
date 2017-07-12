import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/facebook.txt')
dataset.head() ##informacoes sobre a base (colunas etc)
dataset['Date'] = pd.to_datetime(dataset['Date']) ##cast de data
dataset['Variation'] = dataset['Close'].sub(dataset['Open']) ##variacao entre a abertura e o fechamento
print(dataset.head()) ##informacoes gerais sobre o dataset

dataset1 = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/microsoft.txt')
dataset1.head() ##informacoes sobre a base (colunas etc)
dataset1['Date'] = pd.to_datetime(dataset1['Date']) ##cast de data
dataset1['Variation'] = dataset1['Close'].sub(dataset1['Open']) ##variacao entre a abertura e o fechamento
print(dataset1.head()) ##informacoes gerais sobre o dataset

x1=dataset.Date
y1=dataset.Close

z1=dataset1.Date
z2=dataset1.Close

fig, ax = plt.subplots()

ax.plot(z1,z2)
ax.plot(x1,y1)

plt.show()
plt.grid(True)
plt.savefig('imagem.jpeg')
plt.close()




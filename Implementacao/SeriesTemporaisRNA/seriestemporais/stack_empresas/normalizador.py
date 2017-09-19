import pandas as pd
import matplotlib.pyplot as plt


dataset_cisco = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/cisco_normalizado.txt')
dataset_amazon = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/amazon_normalizado.txt')
dataset_microsoft = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/microsoft_normalizado.txt')
dataset_intel = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/intel_normalizado.txt')
dataset_apple = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/apple_normalizado.txt')


dataset_cisco['Date'] = pd.to_datetime(dataset_cisco['Date'])  # repassando o valor para um formato de data
linha = dataset_cisco.Date
coluna = dataset_cisco['Open-normalizado']
coluna1 = dataset_amazon['Open-normalizado']
coluna2 = dataset_microsoft['Open-normalizado']
coluna3 = dataset_intel['Open-normalizado']
coluna4= dataset_apple['Open-normalizado']

fig, ax = plt.subplots()
ax.plot(linha, coluna,  label='Line 2')
ax.plot(linha, coluna1, label='Line 2')
ax.plot(linha, coluna2, label='Line 2')
ax.plot(linha, coluna3, label='Line 2')
ax.plot(linha, coluna4, label='Line 2')
fig.set_size_inches(12, 8, forward=True)
plt.legend(['Cisco', 'Amazon', 'Microsoft', 'Intel', 'Apple'])
plt.grid(True)
plt.show()
plt.close()
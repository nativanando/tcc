import pandas as pd
import matplotlib.pyplot as plt

class Analisador:

    def __init__(self, nome_empresa):
        self.nome_empresa = nome_empresa
        self.criarDataSet()
        self.plotarGrafico()

    def criarDataSet(self):
        self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/'+self.nome_empresa+'.txt')
        self.dataset.head()  ##informacoes sobre a base (colunas etc)
        self.dataset['Date'] = pd.to_datetime(self.dataset['Date'])  ##repassando o valor para um formato de data
        self.dataset['Variation'] = self.dataset['Close'].sub(self.dataset['Open'])  ##Variação entre a abertura e o fechamento

    def plotarGrafico(self):
        self.linha = self.dataset.Date
        self.coluna = self.dataset.Close
        self.fig, self.ax = plt.subplots()
        self.ax.plot(self.linha, self.coluna)
        self.fig.set_size_inches(12, 8, forward=True)
        plt.show()
        plt.grid(True)
        plt.savefig('../assets/'+self.nome_empresa+'.jpeg', pdi=1000)
        plt.close()

import pandas as pd
import matplotlib.pyplot as plt

class Analisador:

    def __init__(self, nome_empresa):
        self.nome_empresa = nome_empresa

    def criarDataSet(self):
        self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/'+self.nome_empresa+'.txt')
        self.dataset.head()  ##informacoes sobre a base (colunas etc)
        self.dataset['Date'] = pd.to_datetime(self.dataset['Date'])  ##cast de data
        self.dataset['Variation'] = self.dataset['Close'].sub(self.dataset['Open'])  ##variacao entre a abertura e o fechamento
        print(self.dataset.head())  ##informacoes gerais sobre o dataset

    def plotarGrafico(self):
        self.linha = self.dataset.Date
        self.coluna = self.dataset.Close
        self.fig, self.ax = plt.subplots()
        self.ax.plot(self.linha, self.coluna)
        self.fig.set_size_inches(8, 6, forward=True)
        plt.show()
        plt.grid(True)
        plt.savefig('../assets/'+self.nome_empresa+'.jpeg', pdi=300)
        plt.close()

analisador = Analisador('microsoft')
analisador.criarDataSet()
analisador.plotarGrafico()

analisador = Analisador('facebook')
analisador.criarDataSet()
analisador.plotarGrafico()

analisador = Analisador('amazon')
analisador.criarDataSet()
analisador.plotarGrafico()

analisador = Analisador('apple')
analisador.criarDataSet()
analisador.plotarGrafico()

analisador = Analisador('google')
analisador.criarDataSet()
analisador.plotarGrafico()

analisador = Analisador('ebay')
analisador.criarDataSet()
analisador.plotarGrafico()

analisador = Analisador('intel')
analisador.criarDataSet()
analisador.plotarGrafico()

analisador = Analisador('cisco')
analisador.criarDataSet()
analisador.plotarGrafico()

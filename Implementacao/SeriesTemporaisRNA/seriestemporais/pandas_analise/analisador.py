"""
analisador.py: Classe responsável por realizar o procedimento de ajustes dos dados coletados, através da biblioteca pandas.
Os métodos implementados manipulam o dataset, criando os indicadores técnicos que serão utilizados como entrada da RNA.
"""
__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"
__version__ = "0.0"

import pandas as pd
import matplotlib.pyplot as plt

class Analisador:

    def __init__(self, nome_empresa):
        self.nome_empresa = nome_empresa
        self.cria_dataset()
        self.plota_grafico_empresa()

    def cria_dataset(self):
        self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/'+self.nome_empresa+'.txt')
        self.dataset.head()  #informacoes sobre a base (colunas etc)
        self.dataset['Date'] = pd.to_datetime(self.dataset['Date'])  #repassando o valor para um formato de data
        self.dataset['movel_26'] = None
        self.dataset['movel_10'] = None

    def plota_grafico_empresa(self):
        self.linha = self.dataset.Date
        self.coluna = self.dataset.Open
        self.fig, self.ax = plt.subplots()
        self.ax.plot(self.linha, self.coluna)
        self.fig.set_size_inches(12, 8, forward=True)
        plt.show()
        plt.grid(True)
        plt.savefig('../assets/'+self.nome_empresa+'_open.jpeg', pdi=1000)
        plt.close()

    def calcula_media_movel(self, dia):
        tamanho_dataset = self.dataset.__len__()
        media_valor = 0 # valor que sera incrementado
        flag_parada = 0
        for i in range(tamanho_dataset):
            if i >= dia -1:
                self.executa_calculo_media_movel(i, dia)

    def executa_calculo_media_movel(self, indice_dataset, dia):
        indice_dataset = indice_dataset + 1
        indice_inicial = indice_dataset - (dia)
        valor_media = 0
        for i in range(indice_dataset):
            if i >= indice_inicial:
                valor_media = valor_media + self.dataset.loc[i].Close
                print ('index:', i)
        self.dataset.set_value(indice_dataset - 1, 'movel_' + str(dia), valor_media / dia, takeable=False)
        self.dataset.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/'+self.nome_empresa+'_calculado.txt')

    def formata_dataset(self):
        self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/'+self.nome_empresa+'_calculado.txt')
        self.dataset.drop(self.dataset.columns[[0]], axis=1, inplace=True)
        for i in range(25):
            self.dataset.drop(i, inplace=True)

        print(self.dataset)
        self.dataset['MACD'] = self.dataset['movel_10'].sub(self.dataset['movel_26']) #calculo do MACS a partir das duas médias móveis
        self.dataset.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/'+self.nome_empresa+'_formatado.txt')

    def calcula_macd(self, dataset):
        dataset['MACD'] = dataset['movel_10'].sub(self.dataset['movel_26'])
        return dataset

    def normaliza_coluna(self, dataset, coluna):
        resultado = []
        for i in range(dataset.__len__()):
            resultado.append((dataset.iloc[i][coluna] - min(dataset[coluna])) / (max(dataset[coluna]) - min(dataset[coluna])))
        dataset[coluna + '-normalizado'] = resultado
        return dataset

    def desnormaliza_valor(self, dataset, coluna, valor):
        valor = valor * max(dataset[coluna]) + (1 - valor) * min(dataset[coluna])
        return valor
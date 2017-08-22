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
        self.dataset['Variation'] = self.dataset['Close'].sub(self.dataset['Open']) #Variação entre a abertura e o fechamento
        self.dataset['movel_26'] = None
        self.dataset['movel_10'] = None

    def plota_grafico_empresa(self):
        self.linha = self.dataset.Date
        self.coluna = self.dataset.Close
        self.fig, self.ax = plt.subplots()
        self.ax.plot(self.linha, self.coluna)
        self.fig.set_size_inches(12, 8, forward=True)
        plt.show()
        plt.grid(True)
        plt.savefig('../assets/'+self.nome_empresa+'.jpeg', pdi=1000)
        plt.close()

    def calcula_media_movel(self, dia):
        '''
        Inicia  o looping do dataset a partir do primeiro dia escolhido (26 ou 10) até o tamanho total do dataset
        Pega o valor atual do indice e o dataset inteiro, colocando-os em outra função
        Entrando nesta função, fazer uma subtração do indice atual - o dia ecolhido, será igual ao índice inicial desse looping
        Fazer o for do dataset na posição inicial que foi calculada até o indice atual, somando os valores de fechamento
        Feito isso, realizar a divisão do valor calculado pela quantidade do dia, calculando assim, a média movel
        '''
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
        print(self.dataset.loc[indice_dataset - 1])
        valor_media = 0
        self.dataset.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/'+self.nome_empresa+'_formatado.txt')

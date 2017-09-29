import pandas as pd
import matplotlib.pyplot as plt

class Normalizador:

    def __init__(self):
        try:
            self.dataset_cisco = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/cisco_normalizado.txt')
            self.dataset_amazon = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/amazon_normalizado.txt')
            self.dataset_microsoft = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/microsoft_normalizado.txt')
            self.dataset_intel = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/intel_normalizado.txt')
            self.dataset_apple = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/apple_normalizado.txt')
        except IOError:
            print("Erro ao abrir os dados das empresas")
            return 0

    def define_linha_coluna(self):
        self.linha = self.dataset_cisco['Date'] = pd.to_datetime(self.dataset_cisco['Date'])
        self.coluna = self.dataset_cisco['Open-normalizado']
        self.coluna1 = self.dataset_amazon['Open-normalizado']
        self.coluna2 = self.dataset_microsoft['Open-normalizado']
        self.coluna3 = self.dataset_intel['Open-normalizado']
        self.coluna4 = self.dataset_apple['Open-normalizado']

    def cria_grafico(self):
        fig, ax = plt.subplots()
        ax.plot(self.linha, self.coluna)
        ax.plot(self.linha, self.coluna1)
        ax.plot(self.linha, self.coluna2)
        ax.plot(self.linha, self.coluna3)
        ax.plot(self.linha, self.coluna4)
        fig.set_size_inches(12, 8, forward=True)
        plt.legend(['Cisco', 'Amazon', 'Microsoft', 'Intel', 'Apple'])
        plt.grid(True)
        plt.show()
        plt.close()

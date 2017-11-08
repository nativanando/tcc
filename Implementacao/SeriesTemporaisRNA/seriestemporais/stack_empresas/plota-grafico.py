import pandas as pd
import matplotlib.pyplot as plt

class Grafico:

    def __init__(self):
        try:
            self.dataset_cisco = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/cisco_formatado.txt')
            self.dataset_amazon = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/amazon_formatado.txt')
            self.dataset_microsoft = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/microsoft_formatado.txt')
            self.dataset_intel = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/intel_formatado.txt')
            self.dataset_apple = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/apple_formatado.txt')
        except IOError:
            print("Erro ao abrir os dados das empresas")
            return 0

    def define_linha_coluna(self):
        self.linha = self.dataset_microsoft['Date'] = pd.to_datetime(self.dataset_cisco['Date'])
        self.coluna = self.dataset_microsoft['Open']


    def cria_grafico(self):
        fig, ax = plt.subplots()
        ax.plot(self.linha, self.coluna)
        fig.set_size_inches(12, 8, forward=True)
        plt.grid(True)
        plt.show()
        plt.close()

if __name__ == '__main__':
    grafico = Grafico()
    grafico.define_linha_coluna()
    grafico.cria_grafico()
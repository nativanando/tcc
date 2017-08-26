import pandas as pd

class Classificador:

    def __init__(self, nome_empresa): ##realiza o calculo da media nativamente pela lib
        self.nome_empresa = nome_empresa
        self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/' + self.nome_empresa + '_formatado.txt')
        print(self.dataset.head())  # informacoes sobre a base (colunas etc)
        media_10_dias = self.dataset['Close'].rolling(window=10, center=False).mean()
        print (media_10_dias)


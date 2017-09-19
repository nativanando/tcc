"""
classificador.py: Classe responsável por realizar o cálculo da média movel de forma nativa, utilizando pandas
"""
__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"
__version__ = "1.0"

import pandas as pd

class Classificador:

    def __init__(self, nome_empresa):
        self.nome_empresa = nome_empresa
        self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_coletados/' + self.nome_empresa + '.txt')
        print(self.dataset.head())  # informacoes sobre a base (colunas etc)
        self.dataset['movel_10'] = self.dataset['Close'].rolling(window=10, center=False).mean()
        self.dataset['movel_26'] = self.dataset['Close'].rolling(window=26, center=False).mean()
        self.dataset['MACD'] = self.dataset['movel_10'].sub(self.dataset['movel_26']) #calculo do MACS a partir das duas médias móveis
        self.dataset.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_coletados/' + self.nome_empresa + '_calculado.txt')
        self.formataDados()

    def formataDados(self):
        self.dataset = pd.read_csv(
            '~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/' + self.nome_empresa + '_formatado.txt')
        self.dataset.drop('id_exclusao', axis=1, inplace=True)
        self.dataset.to_csv(
            '~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/' + self.nome_empresa + '_formatado_novo.txt')
        print(self.dataset)
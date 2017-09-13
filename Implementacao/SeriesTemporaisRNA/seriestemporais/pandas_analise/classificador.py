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
        self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/' + self.nome_empresa + '_formatado.txt')
        print(self.dataset.head())  # informacoes sobre a base (colunas etc)
        media_10_dias = self.dataset['Close'].rolling(window=10, center=False).mean()
        print (media_10_dias)


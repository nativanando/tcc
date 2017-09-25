"""
Crawler.py: Buscador genérico das séries temporais.
"""
__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"
__version__ = "0.0.1"

import pandas_datareader.data as web
import datetime

class Crawler:

    def __init__(self, nome_empresa, codigo):
        self.start = datetime.datetime(2001, 1, 1)
        self.end = datetime.datetime(2017, 8, 31)
        self.nome_empresa = nome_empresa
        self.codigo = codigo

    def executa_busca(self):
        file = web.DataReader(self.codigo, 'google',  self.start, self.end)
        file.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/' + self.nome_empresa + '.txt')
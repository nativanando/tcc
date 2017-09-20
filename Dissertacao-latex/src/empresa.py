import abc
from seriestemporais.stack_empresas.crawler import *

class Empresa(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executa_busca(self):
        pass

class Apple(Empresa):

    def __init__(self):
        self.nome_empresa = 'apple'
        self.codigo = 'AAPL'
        self.executa_busca()

    def executa_busca(self):
        crawler = Crawler(self.nome_empresa, self.codigo)
        crawler.executa_busca()

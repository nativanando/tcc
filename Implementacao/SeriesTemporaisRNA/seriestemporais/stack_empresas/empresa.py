import abc
from seriestemporais.stack_empresas.crawler import *

class Empresa(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executa_busca(self):
        pass

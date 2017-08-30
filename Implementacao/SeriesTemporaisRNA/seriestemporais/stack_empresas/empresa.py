import abc

class Empresa(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executa_busca(self):
        pass
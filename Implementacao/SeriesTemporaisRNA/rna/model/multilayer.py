"""
multilayer.py: Classe responsável por realizar a implementação de uma rede MultiLayer Percepetron utilizando 3 entradas.
Sendo composta por 8 entradas na camada da entrada, 13 neurônios na camada oculta e 1 na camada de saída
A criação desta rede leva em consideração e referência a documentação oficial do PyBrain.
A rede, que é caracterizada por um modelo recorrente, neste caso, teve um treinamento utilizando o algoritmo backpropagation
com as camadas ocultas utilizando a função de ativação do tipo sigmóide.
"""
__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"
__version__ = "1.0"

from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.structure import RecurrentNetwork
import pandas as pd
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader
import timeit
import numpy as np

class MultiLayer:
    def __init__(self, network, camada_entrada, camada_oculta, camada_saida, nome_empresa):
        self.network = network
        self.network = RecurrentNetwork()
        self.camada_entrada = camada_entrada
        self.camada_oculta = camada_oculta
        self.camada_saida = camada_saida
        self.nome_empresa = nome_empresa
        self.ligacao_entrada_oculta = None
        self.ligacao_oculta_saida = None
        self.defineArquitetura()

    def defineArquitetura(self):
        self.camada_entrada = LinearLayer(self.camada_entrada, name="entrada")
        self.camada_oculta = SigmoidLayer(self.camada_oculta, name="oculta")
        self.camada_saida = LinearLayer(self.camada_saida, name="saida")
        self.adicionaEstrutura()

    def adicionaEstrutura(self):
        self.network.addInputModule(self.camada_entrada)
        self.network.addModule(self.camada_oculta)
        self.network.addOutputModule(self.camada_saida)
        self.adicionaConexoes()

    def adicionaConexoes(self):
        self.ligacao_entrada_oculta = FullConnection(self.camada_entrada, self.camada_oculta)
        self.ligacao_oculta_saida = FullConnection(self.camada_oculta, self.camada_saida)
        self.network.addConnection(self.ligacao_oculta_saida)
        self.network.addConnection(self.ligacao_entrada_oculta)
        self.iniciaRede()

    def visualizaPesosSinapticos(self):
        print('peso camada_entrada_oculta',
              self.ligacao_entrada_oculta.params)  # mostra os pesos das conexões de entrada para camada oculta, todas interligadas entre sí. 3x4 = 12 pesos sinpaticos
        print('peso camada_oculta_saida',
              self.ligacao_oculta_saida.params)  # mostra os pesos das conexões da camada oculta para a camada de saída. Todas interligadas entre sí. 3x1 = 3 pesos sinapticos
        print('pesos rede', self.network.params)

    def iniciaRede(self):
        self.network.sortModules()

    def adicionaDadosTreinamento(self):
        self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/' + self.nome_empresa + '_formatado.txt',header=0)
        self.dataset.drop('Date', axis=1, inplace=True)
        self.dataset['Open-normalizado'] = (self.dataset['Open'] - min(self.dataset['Open'])) / (max(self.dataset['Open']) - min(self.dataset['Open']))
        self.dataset['High-normalizado'] = (self.dataset['High'] - min(self.dataset['High'])) / (max(self.dataset['High']) - min(self.dataset['High']))
        self.dataset['Low-normalizado'] = (self.dataset['Low'] - min(self.dataset['Low'])) / (max(self.dataset['Low']) - min(self.dataset['Low']))
        self.dataset['Close-normalizado'] = (self.dataset['Close'] - min(self.dataset['Close'])) / (max(self.dataset['Close']) - min(self.dataset['Close']))
        self.dataset['Volume-normalizado'] = (self.dataset['Volume'] - min(self.dataset['Volume'])) / (max(self.dataset['Volume']) - min(self.dataset['Volume']))
        self.dataset['movel_26-normalizado'] = (self.dataset['movel_26'] - min(self.dataset['movel_26'])) / (max(self.dataset['movel_26']) - min(self.dataset['movel_26']))
        self.dataset['movel_10-normalizado'] = (self.dataset['movel_10'] - min(self.dataset['movel_10'])) / (max(self.dataset['movel_10']) - min(self.dataset['movel_10']))
        self.dataset['MACD-normalizado'] = (self.dataset['MACD'] - min(self.dataset['MACD'])) / (max(self.dataset['MACD']) - min(self.dataset['MACD']))
        self.dataset.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/' + self.nome_empresa + '_normalizado.txt')
        self.dataset_treino = SupervisedDataSet(8, 1)

        for i in range(self.dataset.__len__() - 1):
            self.dataset_treino.addSample([self.dataset.iloc[i]['Open-normalizado'], self.dataset.iloc[i]['High-normalizado'],
            self.dataset.iloc[i]['Low-normalizado'],self.dataset.iloc[i]['Close-normalizado'], self.dataset.iloc[i]['Volume-normalizado'],
            self.dataset.iloc[i]['movel_26-normalizado'], self.dataset.iloc[i]['movel_10-normalizado'], self.dataset.iloc[i]['MACD-normalizado']],
            self.dataset.iloc[i + 1]['Open-normalizado'])

        self.realizaTreinamento()

    def realizaTreinamento(self):
        trainer = BackpropTrainer(self.network, self.dataset_treino, verbose=True, learningrate=0.01, momentum=0.99)
        start = timeit.default_timer()

        for epoch in range(0, 1000):  # treina por 1000 iterações para ajuste de pesos
            resultTrainer = trainer.train()

        NetworkWriter.writeToFile(self.network, 'rede2.xml')

        valor_abertura2 = (self.network.activate([37.87, 38.0, 37.52, 37.8, 32357313, 36.7930769231, 36.971, 0.17792307689999376]))  # penultima - 1 #37.82 resultado #[ 0.90872757]
        print("valor abertura", valor_abertura2[0])
        resultadorede2 = valor_abertura2[0] * max(self.dataset['Open']) + (1 - valor_abertura2[0]) * min(self.dataset['Open'])
        print("resultado", resultadorede2)
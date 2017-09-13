from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised import BackpropTrainer
import timeit
import pandas as pd
from PIL import Image
from pytesseract import *

__author__ = 'Fernando Natividade.'

'''
MLP utilizando 3 entradas, 4 neuronios na camada oculta e 1 saídas
A criação desta rede leva em consideração e referência a documentação oficial do PyBrain.
A rede, que é caracterizada por um modelo FeedFoward, neste caso, teve um treinamento utilizando o algoritmo backpropagation,
com as camadas ocultas utilizando a função de ativação sigmoide nos neurônios da camada oculta
'''


class FeedFoward:
    def __init__(self, network, camada_entrada, camada_oculta, camada_saida):
        self.network = network
        self.network = FeedForwardNetwork()
        self.camada_entrada = camada_entrada
        self.camada_oculta = camada_oculta
        self.camada_saida = camada_saida
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


dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/intel_formatado.txt')
dataset_treino = SupervisedDataSet(8, 1)
for i in range(dataset.__len__() - 1):
    dataset_treino.addSample([dataset.iloc[i]['Open'], dataset.iloc[i]['High'], dataset.iloc[i]['Low'],
    dataset.iloc[i]['Close'], dataset.iloc[i]['Volume'], dataset.iloc[i]['movel_26'],
    dataset.iloc[i]['movel_10'], dataset.iloc[i]['MACD']], dataset.iloc[i + 1]['Open'])

network = None
rna = FeedFoward(network, 8, 13, 1)

trainer = BackpropTrainer(rna.network, dataset_treino, verbose=True, learningrate=0.01, momentum=0.99)
start = timeit.default_timer()

for epoch in range(0, 100):  # treina por 1000 iterações para ajuste de pesos
    resultTrainer = trainer.train()

stop = timeit.default_timer()
print(resultTrainer)
rna.visualizaPesosSinapticos()
print ("tempo de execução", stop - start)

##test_data = SupervisedDataSet(4, 1)
##test_data.addSample([1, 1, 0, 1], [0])
##test_data.addSample([1, 1, 0, 1], [0])
##test_data.addSample([0, 0, 1, 1], [0])
##test_data.addSample([0, 0, 1, 1], [0])

##result = trainer.testOnData(test_data, verbose=True)  # verbose=True indica que deve ser impressas mensagens
##erroMedio = result
##print ("erro medio encontrado no teste", erroMedio)
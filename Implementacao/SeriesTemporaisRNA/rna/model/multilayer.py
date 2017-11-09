"""
multilayer.py: Classe responsável por realizar a implementação de uma rede MultiLayer Percepetron utilizando 3 entradas.
Sendo composta por 8 entradas na camada da entrada, 13 neurônios na camada oculta e 1 na camada de saída
A criação desta rede leva em consideração e referência a documentação oficial do PyBrain.
A rede, que é caracterizada por um modelo recorrente, neste caso, teve um treinamento utilizando o algoritmo backpropagation
com as camadas ocultas utilizando a função de ativação do tipo sigmóide.
"""
__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"
__version__ = "0.0.1"

from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.structure import FeedForwardNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader
import pandas as pd
import matplotlib.pyplot as plt
import time



class MultiLayer:
    def __init__(self, network, camada_entrada, camada_oculta, camada_saida, nome_empresa):
        self.network = network
        self.network = FeedForwardNetwork()
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
        print('pesos rede', self.network.params)

    def iniciaRede(self):
        self.network.sortModules()

    def adicionaDadosTreinamento(self):
        try:
            self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/'
                                       + self.nome_empresa + '_normalizado.txt',header=0)
        except IOError:
            print ("Erro ao abrir os dados da empresa "+self.nome_empresa+"")
            return 0

        self.dataset.drop('Date', axis=1, inplace=True)
        self.dataset_teste = self.dataset.iloc[4117:4125]

        self.dataset_treino = SupervisedDataSet(8, 1)
        print(self.dataset.iloc[1]['Open-normalizado'])
        print(self.dataset.iloc[2]['Open'])

        for i in range(self.dataset.__len__() - 8):
            self.dataset_treino.addSample([self.dataset.iloc[i]['Open-normalizado'], self.dataset.iloc[i]['High-normalizado'],
                                           self.dataset.iloc[i]['Low-normalizado'],
                                           self.dataset.iloc[i]['Close-normalizado'], self.dataset.iloc[i]['Volume-normalizado'],
                                           self.dataset.iloc[i]['movel_26-normalizado'],
                                           self.dataset.iloc[i]['movel_10-normalizado'], self.dataset.iloc[i]['MACD-normalizado']],
                                           self.dataset.iloc[i + 1]['Open-normalizado'])

    def realizaTreinamento(self):
        inicio = time.time()
        error = []
        indice = []
        self.trainer = BackpropTrainer(self.network, self.dataset_treino, learningrate=0.4, verbose=True)
        for i in range (1000):
            erro_quadratico = self.trainer.train()
            error.append(erro_quadratico)
            indice.append(i)
        fim = time.time()
        print(fim - inicio)
        NetworkWriter.writeToFile(self.network, 'snapshot_redes/rede-feedforward-'+self.nome_empresa+'1000_tempo.xml')
        self.plotaGraficoErro(indice, error)

    def testaRede(self):
        base_teste = SupervisedDataSet(8, 1)

        for i in range(self.dataset_teste.__len__() - 1):
            base_teste.addSample([self.dataset_teste.iloc[i]['Open-normalizado'], self.dataset_teste.iloc[i]['High-normalizado'],
                                  self.dataset_teste.iloc[i]['Low-normalizado'],
                                  self.dataset_teste.iloc[i]['Close-normalizado'], self.dataset_teste.iloc[i]['Volume-normalizado'],
                                  self.dataset_teste.iloc[i]['movel_26-normalizado'],
                                  self.dataset_teste.iloc[i]['movel_10-normalizado'],
                                  self.dataset_teste.iloc[i]['MACD-normalizado']], self.dataset_teste.iloc[i+1]['Open-normalizado'])

        erro, result = self.trainer.testOnData(base_teste, verbose=True)
        print ("erro", result[1][0][0])
        self.resultado_rede = result;

    def testarRedeEmpresa(self):
        try:
            rede = NetworkReader.readFrom('snapshot_redes/rede-feedforward-'+self.nome_empresa+'1000_tempo.xml')
            self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/'
                                  + self.nome_empresa + '_normalizado.txt',header=0)
            print ('sadasda', max(self.dataset['Open-normalizado']))
        except IOError:
            print ("Erro ao abrir os arquivo da rede neural")
            return 0

        print (self.dataset.__len__())
        self.dataset_teste = self.dataset.iloc[4117:4125]
        self.trainer = BackpropTrainer(rede)
        base_teste = SupervisedDataSet(8, 1)

        for i in range(self.dataset_teste.__len__() - 1):
            base_teste.addSample([self.dataset_teste.iloc[i]['Open-normalizado'], self.dataset_teste.iloc[i]['High-normalizado'],
                                  self.dataset_teste.iloc[i]['Low-normalizado'],
                                  self.dataset_teste.iloc[i]['Close-normalizado'], self.dataset_teste.iloc[i]['Volume-normalizado'],
                                  self.dataset_teste.iloc[i]['movel_26-normalizado'],
                                  self.dataset_teste.iloc[i]['movel_10-normalizado'],
                                  self.dataset_teste.iloc[i]['MACD-normalizado']], self.dataset_teste.iloc[i+1]['Open-normalizado'])

        erro, result = self.trainer.testOnData(base_teste, verbose=True)
        self.resultado_rede = result
        print(self.resultado_rede.__len__())
        for i in range (self.resultado_rede.__len__()):
            resultadorede = self.resultado_rede[i][0][0] * max(self.dataset['Open']) +\
                             (1 - self.resultado_rede[i][0][0] ) * min(self.dataset['Open'])
            resultado_esperado = self.dataset_teste.iloc[i + 1]['Open']
            print ("resultado esperado: ",resultado_esperado)
            print("%.2f" % resultadorede)

    def plotaGraficoErro(self, indice, erro):
        print (indice)
        print (erro)
        plt.plot(indice, erro)
        plt.yscale('log')
        plt.xlabel('Iterações')
        plt.ylabel('Erro quadrático médio')
        plt.grid(True)
        plt.show()

    def plotaGraficoResultado(self):
        try:
            dados = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/resultado_series/'
                                       + self.nome_empresa + '_predicao.txt', header=0)
            print(dados)
        except IOError:
            print("Erro ao abrir o arquivo de resultados")
            return 0

        dados['Data'] = pd.to_datetime(dados['Data'], format="%d-%m-%Y")
        linha = dados['Data']
        coluna = dados['Abertura']
        coluna1 = dados['Predição']
        fig, ax = plt.subplots()
        ax.plot(linha, coluna, 'go')  # green bolinha
        ax.plot(linha, coluna1, 'ro')  # green bolinha
        fig.set_size_inches(12, 8, forward=True)
        plt.legend(['Valor de abertura', 'Predição'])
        ax.plot(linha, coluna, 'k:', color='orange')  # linha pontilha orange
        ax.plot(linha, coluna1, 'k:', color='blue')  # linha pontilha orange
        plt.grid(True)
        plt.show()
        plt.close()


if __name__ == '__main__':
    network = None
    rna = MultiLayer(network, 8, 13, 1, "intel")
    rna.adicionaDadosTreinamento()
    rna.realizaTreinamento()
    rna.testaRede()
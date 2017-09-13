from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.structure import RecurrentNetwork
import pandas as pd
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader
from pandas import Series
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import math


def importaRedeTeste():
        net = NetworkReader.readFrom('rede.xml')
        print('pesos rede', net.params)
        dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/intel_formatado.txt')
        dataset_treino = SupervisedDataSet(8, 1)
        for i in range(dataset.__len__() - 1):
            dataset_treino.addSample(
                [dataset.iloc[i]['Open'], dataset.iloc[i]['High'], dataset.iloc[i]['Low'],
                 dataset.iloc[i]['Close'], dataset.iloc[i]['Volume'], dataset.iloc[i]['movel_26'],
                 dataset.iloc[i]['movel_10'], dataset.iloc[i]['MACD']], dataset.iloc[i + 1]['Open'])

        trainer = BackpropTrainer(net, dataset_treino, verbose=True, learningrate=0.01, momentum=0.99)
        for epoch in range(0, 1000):  # treina por 1000 iterações para ajuste de pesos
            resultTrainer = trainer.train()

        print(resultTrainer)
        test_data3 = SupervisedDataSet(8, 1)
        test_data3.addSample([37.87, 38.0, 37.52, 37.8, 32357313, 36.7930769231, 36.971, 0.17792307689999376],[37.82])  # saida 1 //erro //correct é a sequencia colocada e out e a saída da rede

        resultado1 = trainer.testOnData(test_data3, verbose=True)

def normalizaDataSet(nome_empresa):
    # Normalize time series data
    # load the dataset and print the first 5 rows
    series = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/'+nome_empresa+'_formatado.txt', header=0)
    series.drop('Date', axis=1, inplace=True)
    series['Open-normalizado'] = (series['Open'] - min(series['Open'])) / (max(series['Open']) - min(series['Open']))
    series['High-normalizado'] = (series['High'] - min(series['High'])) / (max(series['High']) - min(series['High']))
    series['Low-normalizado'] = (series['Low'] - min(series['Low'])) / (max(series['Low']) - min(series['Low']))
    series['Close-normalizado'] = (series['Close'] - min(series['Close'])) / (max(series['Close']) - min(series['Close']))
    series['Volume-normalizado'] = (series['Volume'] - min(series['Volume'])) / (max(series['Volume']) - min(series['Volume']))
    series['movel_26-normalizado'] = (series['movel_26'] - min(series['movel_26'])) / (max(series['movel_26']) - min(series['movel_26']))
    series['movel_10-normalizado'] = (series['movel_10'] - min(series['movel_10'])) / (max(series['movel_10']) - min(series['movel_10']))
    series['MACD-normalizado'] = (series['MACD'] - min(series['MACD'])) / (max(series['MACD']) - min(series['MACD']))
    series.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/'+nome_empresa+'_normalizado.txt')
    print (series['Open-normalizado'].iloc[1])
    print (series.iloc[2]['Open'])
    net = NetworkReader.readFrom('rede.xml')
    print('pesos rede', net.params)
    dataset_treino = SupervisedDataSet(8, 1)
    for i in range(series.__len__() - 1):
        dataset_treino.addSample(
            [series.iloc[i]['Open-normalizado'], series.iloc[i]['High-normalizado'], series.iloc[i]['Low-normalizado'],
             series.iloc[i]['Close-normalizado'], series.iloc[i]['Volume-normalizado'], series.iloc[i]['movel_26-normalizado'],
             series.iloc[i]['movel_10-normalizado'], series.iloc[i]['MACD-normalizado']], series.iloc[i+1]['Open-normalizado'])

    trainer = BackpropTrainer(net, dataset_treino, verbose=True, learningrate=0.01, momentum=0.99)
    for epoch in range(0, 1000):  # treina por 1000 iterações para ajuste de pesos
        resultTrainer = trainer.train()

    NetworkWriter.writeToFile(net, 'rede2.xml')

    valor_abertura2 = (net.activate([37.87, 38.0, 37.52, 37.8, 32357313, 36.7930769231, 36.971,0.17792307689999376]))  # penultima - 1 #37.82 resultado #[ 0.90872757]
    print("valor abertura", valor_abertura2[0])
    resultadorede2 = valor_abertura2[0] * max(series['Open']) + (1 - valor_abertura2[0]) * min(series['Open'])
    print("resultado", resultadorede2)


if __name__ == '__main__':
    normalizaDataSet('intel')

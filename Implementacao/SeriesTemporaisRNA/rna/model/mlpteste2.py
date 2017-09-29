import pandas as pd
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

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
        for epoch in range(0, 10000):  # treina por 1000 iterações para ajuste de pesos
            resultTrainer = trainer.train()

        print(resultTrainer)
        test_data3 = SupervisedDataSet(8, 1)
        test_data3.addSample([37.87, 38.0, 37.52, 37.8, 32357313, 36.7930769231, 36.971, 0.17792307689999376],[37.82])  # saida 1 //erro //correct é a sequencia colocada e out e a saída da rede

        resultado1 = trainer.testOnData(test_data3, verbose=True)

def normalizaDataSet(nome_empresa):
    import matplotlib as plt

    # Normalize time series data
    # load the dataset and print the first 5 rows
    series = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/'+nome_empresa+'_normalizado.txt', header=0)
    resultado = []
    print (series['Open-normalizado'].iloc[1])
    series_teste = series.iloc[4117:4124]
    resultadorede2 = 0.876 * max(series['Open']) + (1 - 0.876) * min(series['Open'])
    print ("correta", resultadorede2)

    resultadorede2 = 0.885 * max(series['Open']) + (1 - 0.885) * min(series['Open'])
    print ("predição", resultadorede2)

    print (series.iloc[2]['Open'])
    net = NetworkReader.readFrom('rede-feedfoward.xml')
    print('pesos rede', net.params)
    dataset_treino = SupervisedDataSet(8, 1)
    for i in range(series.__len__() - 8):
        dataset_treino.addSample(
            [series.iloc[i]['Open-normalizado'], series.iloc[i]['High-normalizado'], series.iloc[i]['Low-normalizado'],
             series.iloc[i]['Close-normalizado'], series.iloc[i]['Volume-normalizado'], series.iloc[i]['movel_26-normalizado'],
             series.iloc[i]['movel_10-normalizado'], series.iloc[i]['MACD-normalizado']], series.iloc[i+1]['Open-normalizado'])

    trainer = BackpropTrainer(net, dataset_treino, verbose=True, learningrate=0.01, momentum=0.99)
    for epoch in range(0, 1000):  # treina por 1500 iterações para ajuste de pesos
        resultTrainer = trainer.train()
        print ("result treinamento epoca ",resultTrainer)
        resultado.append(resultTrainer)
    #NetworkWriter.writeToFile(net, 'rede2.xml')

    test_data = SupervisedDataSet(8, 1)

    for i in range(series_teste.__len__() - 1):
        test_data.addSample([series_teste.iloc[i]['Open-normalizado'], series_teste.iloc[i]['High-normalizado'],
        series_teste.iloc[i]['Low-normalizado'],
        series_teste.iloc[i]['Close-normalizado'], series_teste.iloc[i]['Volume-normalizado'],
        series_teste.iloc[i]['movel_26-normalizado'],
        series_teste.iloc[i]['movel_10-normalizado'], series_teste.iloc[i]['MACD-normalizado']],series_teste.iloc[i]['Open-normalizado'])

    result = trainer.testOnData(test_data, verbose=True)


if __name__ == '__main__':
    normalizaDataSet('intel')

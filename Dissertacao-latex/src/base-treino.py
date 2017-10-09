def adicionaDadosTreinamento(self, nome_empresa):
    import pandas as pd
    from pybrain.datasets import SupervisedDataSet

    try:
        self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/'+ nome_empresa + '_normalizado.txt',header=0)
    except IOError:
        print ("Erro ao abrir os dados da empresa "+nome_empresa+"")
        return 0

    self.dataset_treino = SupervisedDataSet(8, 1)

    for i in range(self.dataset.__len__() - 8):
        self.dataset_treino.addSample([
				self.dataset.iloc[i]['Open-normalizado'],
 				self.dataset.iloc[i]['High-normalizado'],
        self.dataset.iloc[i]['Low-normalizado'], 
				self.dataset.iloc[i]['Close-normalizado'],
 				self.dataset.iloc[i]['Volume-normalizado'],
        self.dataset.iloc[i]['movel_26-normalizado'],
 				self.dataset.iloc[i]['movel_10-normalizado'],
        self.dataset.iloc[i]['MACD-normalizado']],
        self.dataset.iloc[i + 1]['Open-normalizado'])

    return self.dataset_treino

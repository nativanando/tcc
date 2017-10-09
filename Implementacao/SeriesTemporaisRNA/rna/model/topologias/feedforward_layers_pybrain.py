from pybrain.structure import LinearLayer, SigmoidLayer


class FeedForwardNetworkPyBrainLayers:

    def __init__(self, tamanho_camada_entrada, tamanho_camada_oculta, tamanho_camada_saida):
        self.camada_entrada = LinearLayer(self.camada_entrada, name="entrada")
        self.camada_oculta = SigmoidLayer(self.camada_oculta, name="oculta")
        self.camada_saida = LinearLayer(self.camada_saida, name="saida")

    def adicionaEstrutura(self, rede):
        rede.addInputModule(self.camada_entrada)
        rede.addModule(self.camada_oculta)
        rede.addOutputModule(self.camada_saida)
        return rede

    def adicionaConexoes(self):
        from pybrain.structure import FullConnection
        '''Importação do objeto FullConnection através do módulo pybrain.structure '''
        self.ligacao_entrada_oculta = FullConnection(self.camada_entrada, self.camada_oculta)
        self.ligacao_oculta_saida = FullConnection(self.camada_oculta, self.camada_saida)
        self.network.addConnection(self.ligacao_oculta_saida)
        self.network.addConnection(self.ligacao_entrada_oculta)
        self.iniciaRede()

    def adicionaDadosTreinamento(self, nome_empresa):
        import pandas as pd
        from pybrain.datasets import SupervisedDataSet

        try:
            self.dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/'
                                       + nome_empresa + '_normalizado.txt',header=0)
        except IOError:
            print ("Erro ao abrir os dados da empresa "+nome_empresa+"")
            return 0

        self.dataset.drop('Date', axis=1, inplace=True)
        self.dataset_treino = SupervisedDataSet(8, 1)

        for i in range(self.dataset.__len__() - 8):
            self.dataset_treino.addSample([self.dataset.iloc[i]['Open-normalizado'], self.dataset.iloc[i]['High-normalizado'],
                                           self.dataset.iloc[i]['Low-normalizado'],
                                           self.dataset.iloc[i]['Close-normalizado'], self.dataset.iloc[i]['Volume-normalizado'],
                                           self.dataset.iloc[i]['movel_26-normalizado'],
                                           self.dataset.iloc[i]['movel_10-normalizado'], self.dataset.iloc[i]['MACD-normalizado']],
                                           self.dataset.iloc[i + 1]['Open-normalizado'])
        return self.dataset_treino
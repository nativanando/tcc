def adicionaConexoes(self):
    from pybrain.structure import FullConnection
    '''Importação do objeto FullConnection através do módulo pybrain.structure '''
    self.ligacao_entrada_oculta = FullConnection(self.camada_entrada, self.camada_oculta)
    self.ligacao_oculta_saida = FullConnection(self.camada_oculta, self.camada_saida)
    self.network.addConnection(self.ligacao_oculta_saida)
    self.network.addConnection(self.ligacao_entrada_oculta)

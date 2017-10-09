def adicionaEstrutura(self, rede):
    rede.addInputModule(self.camada_entrada)
    rede.addModule(self.camada_oculta)
    rede.addOutputModule(self.camada_saida)
    return rede

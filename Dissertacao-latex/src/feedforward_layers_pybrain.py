from pybrain.structure import LinearLayer, SigmoidLayer

class FeedForwardNetworkPyBrainLayers:

    def __init__(self, tamanho_camada_entrada, tamanho_camada_oculta, tamanho_camada_saida):
        self.camada_entrada = LinearLayer(self.camada_entrada, name="entrada")
        self.camada_oculta = SigmoidLayer(self.camada_oculta, name="oculta")
        self.camada_saida = LinearLayer(self.camada_saida, name="saida")
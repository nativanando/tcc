def realizaTreinamento(self, rede, dataset_treino, epocas, nome_empresa):
    from pybrain.supervised import BackpropTrainer
    from pybrain.tools.customxml import NetworkWriter
        
    treinamento = BackpropTrainer(rede, dataset_treino, learningrate=0.4, verbose=True)
    treinamento.trainEpochs(epochs = epocas)
    NetworkWriter.writeToFile(rede, 'snapshot_redes/rede-feedforward-' + nome_empresa + '.xml')

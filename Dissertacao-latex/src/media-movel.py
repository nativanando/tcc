def executa_calculo_media_movel(self, indice_dataset, dia):
    indice_dataset = indice_dataset + 1
    indice_inicial = indice_dataset - (dia)
    valor_media = 0
    for i in range(indice_dataset):
        if i >= indice_inicial:
        valor_media = valor_media + self.dataset.loc[i].Close
    self.dataset.set_value(indice_dataset - 1, 'movel_' + str(dia), valor_media / dia, takeable=False)
    self.dataset.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/'+self.nome_empresa+'_calculado.txt')

def normaliza_coluna(self, dataset, coluna):
    resultado = []
    for i in range(dataset.__len__()):
        resultado.append((dataset.iloc[i][coluna] - min(dataset[coluna])) / (max(dataset[coluna]) - min(dataset[coluna])))
    dataset[coluna + '-normalizado'] = resultado
    return dataset

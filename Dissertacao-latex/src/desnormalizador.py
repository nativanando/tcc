def desnormaliza_valor(self, dataset, coluna, valor):
    valor = valor * max(dataset[coluna]) + (1 - valor) * min(dataset[coluna])
    return valor

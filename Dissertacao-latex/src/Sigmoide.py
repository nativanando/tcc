def sigmoid(self, entradas):
    self.resultado = []
    for entrada in entradas:
        self.resultado.append(1/(1+math.exp(-entrada)))
    return self.resultado

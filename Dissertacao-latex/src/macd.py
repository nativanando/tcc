def calcula_macd(self, dataset):
    dataset['MACD'] = dataset['movel_10'].sub(self.dataset['movel_26'])
    return dataset

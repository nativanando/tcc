import pandas_datareader.data as web
import datetime

start = datetime.datetime(2001, 03, 05)
end = datetime.datetime(2001, 04, 11)

dataset = web.DataReader("MSFT", 'google', start, end)
dataset.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/msft.csv')

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2001, 03, 05)
end = datetime.datetime(2001, 04, 11)

f = web.DataReader("MSFT", 'google', start, end)
f.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/microsoft.txt')

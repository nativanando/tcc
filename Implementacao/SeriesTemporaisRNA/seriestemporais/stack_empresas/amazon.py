"""
amazon.py: Classe responsável por realizar a coleta das ações da amazon.
"""
__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"
__version__ = "1.0"

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2001, 1, 1)
end = datetime.datetime(2017, 1, 27)

f = web.DataReader("AMZN", 'google', start, end)
f.to_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/amazon.txt')

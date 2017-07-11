import pandas as pd
import plotly.offline as py
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='nativanando', api_key='jT97SpDbDMxAEXWmBhyM')


dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados/facebook.txt')
dataset.head() ##informacoes sobre a base (colunas etc)
dataset['Date'] = pd.to_datetime(dataset['Date']) ##cast de data
dataset['Variation'] = dataset['Close'].sub(dataset['Open']) ##variacao entre a abertura e o fechamento
print(dataset.head()) ##informacoes gerais sobre o dataset

x1= dataset.Date
y1=dataset.Close
data = [go.Scatter(x=x1, y=y1)]
layout = go.Layout(
   xaxis=dict(
       range=['01-01-2010','11-04-2017'],
       title='Ano'
   ),
   yaxis=dict(
       range=[min(x1), max(y1)],
       title='Valor da Acao'
   ))
fig = go.Figure(data = data, layout = layout)
py.iplot(fig)



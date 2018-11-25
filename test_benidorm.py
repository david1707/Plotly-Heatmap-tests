import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Benidorm.csv')

data = [go.Heatmap(x=df['Day'], y=df['Hour'], z=df['Temperature'], autocolorscale=None)]
layout = go.Layout(title='Benidorm Weekly Temperatures')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='benidorm.html', include_plotlyjs='cdn')

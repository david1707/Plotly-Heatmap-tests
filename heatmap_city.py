import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import sys

try:
    city = sys.argv[1]
except:
    city = 'Benidorm'

try:
    df = pd.read_csv(f'{city}.csv')

    data = [go.Heatmap(x=df['Day'], y=df['Hour'], z=df['Temperature'])]
    layout = go.Layout(title=f'{city} Weekly Temperatures', xaxis=dict(title='Day'), yaxis=dict(title='Celsius Degrees'))

    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig, filename=f'{city}.html', include_plotlyjs='cdn')
except FileNotFoundError:
    print(f'{city}.csv file not found.')

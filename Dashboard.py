from dash import Dash, html, dcc, Input, Output, State, callback, dash_table
import plotly.graph_objects as go
import pandas as pd

from import_data import import_tempature

# Data import
df = import_tempature.import_data()
df_year = import_tempature.import_slicer()

##### Initial the app #####
app = Dash(__name__)

###### App layout #####
app.layout = html.Div([
    html.H1(children='Temperaturdaten'),
    dcc.Graph(id='output-TMK'),
    dcc.RadioItems(df_year, '1988', id='input-year')
])

##### Callback #####
@callback(
    Output('output-TMK', 'figure'),
    Input('input-year', 'value')
)
def update_figure(input_year):
    dff = df[df.Year == input_year]
    layout = go.Layout(
        title={'text': 'Temperaturdatenverlauf',
               'x': 0.5,
               'y': 0.85,
               'xanchor': 'center'},
        xaxis=dict(title="Datum"),
        yaxis=dict(title="Durschnittliche Temperatur [°C]"),
        template='plotly_dark'  # "plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"
    )
    fig = go.Figure(layout=layout)
    fig.add_trace(
        go.Scatter(x=dff['MESS_DATUM'], y=dff['TMK'])
    )
    return fig


##### Run the app #####
if __name__ == '__main__':
    app.run(debug=True)
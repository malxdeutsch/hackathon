import dash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import yfinance as yf
import plotly.express as px

app = dash.Dash()

app.layout = html.Div([

    html.H3('Stock Tickers'),
    
    dcc.Input(
            id = 'text_input',
            # id='input_{}'.format(_),
            type= 'text',
            placeholder= 'Stock Name',
        ),
    dcc.Dropdown(
        id = 'my-dropdown',
        options= [
            {'label' : 'Run', 'value': 'Run'},
        ],
        value =''
    ),

    dcc.Graph (id= 'my-graph')
    ])

@app.callback(Output('my-graph', 'figure'), [Input('text_input', 'value'), Input('my-dropdown', 'value')])
def update_graph(text_input, run):
    if run == 'Run':
        df= yf.download(text_input)
    # df = yf.Ticker(selected_dropdown_value)
    # df = px.data.stocks()

    figure = {
        'data' : [{
            'x' : df.index,
            'y' : df.Close
        }],
        'layout':{
            'title':text_input,
            'xaxis':{
                'title':'Closing Value'
                },
            'yaxis':{
                'title':'date'
                }
            }
    
    }
    return figure
if __name__ == '__main__':
    app.run_server()
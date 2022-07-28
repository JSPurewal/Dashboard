#Import Libraries
import dash
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

#Load dataset
df = pd.read_csv("myntra_products_catalog.csv")

#create dash app
app = dash.Dash(__name__)


#set up layout
app.layout=html.Div([#container component
    html.H1("Myntra Gender Based Product Range"),
    dcc.Dropdown(id='gender-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df.Gender.unique())],
                 value='Men',
                 style={'width':'50%'}
                 ),

    dcc.Graph(id='my-graph',
              figure={}),
    dcc.Graph(id='my-graph1',
              figure={}),

])

#setup callback functions
@app.callback(#decorator
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='gender-choice', component_property='value'),
)
def interactive_graphs(value_gender):
    dff = df[df.Gender==value_gender]
    fig = px.histogram(data_frame=dff, x='ProductBrand', y='NumImages',color_discrete_sequence=['indianred'])

    return fig

@app.callback(
    Output(component_id='my-graph1', component_property='figure'),
    Input(component_id='gender-choice', component_property='value'),
)
def interactive_graphs(value_gender):
    dff = df[df.Gender==value_gender]
    dff=dff[dff.Price < 1000]
    fig1 = px.histogram(data_frame=dff, x='ProductBrand', y='NumImages')

    return fig1




#run local server

app.run_server()

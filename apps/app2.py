# import plotly.graph_objects as go
import pandas as pd
from data_files import india_data
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly_express as px
from app import app

# needed if running single page dash app instead
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(india_data, index_col = 0)

# preparing various dataframes for visualisation
from datetime import datetime
# df.index = pd.to_datetime(df.index, format='%d/%m/%y')
# df = df.sort_index()
# convert number of cases and deaths to per 1 million population figures
# to allow for comparison
# df['cases per 1 mil'] = df['cases']/df['popData2018']*1000000
# df['deaths per 1 mil'] = df['deaths']/df['popData2018']*1000000
# exclude observations from the Japan cruise ship
# df = df[df.continentExp != 'Other']

# df2 = df.copy()
# df2 = df2.groupby(['continentExp','date']).sum()
#
# df2 = df2.sort_values(['date'], ascending = True)
# df3 = df2.copy()
# df3 = df3.tail(5)
# df3 = df3.reset_index()
#
# df4 = df.copy()
# df4 = df4.groupby(['continentExp']).sum()
#
# # cumulative cases and deaths
# df5 = df.copy()
# df5 = df5.groupby(['continentExp','date']).sum()
# df5 = df5.reset_index()
# df5['cases per 1 mil'] = df5.groupby(['continentExp'])['cases per 1 mil'].apply(lambda x: x.cumsum())
# df5['deaths per 1 mil'] = df5.groupby(['continentExp'])['deaths per 1 mil'].apply(lambda x: x.cumsum())

# good if there are many options
available_states = df['State/UnionTerritory'].unique()
avail_col = ["Confirmed", "Deaths", "Cured"]
# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='COVID-19 India Dashboard'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Visualising COVID-19 India Data'), className="mb-4")
        ]),
# choose between cases or deaths
    dcc.Dropdown(
        id='state',
        options=[
            {'label': i, 'value': i} for i in available_states
        ],
        value='Telengana',
        #multi=True,
        style={'width': '50%'}
        ),
# for some reason, font colour remains black if using the color option
    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='Total Cases in India',id="st_lab",
                                 className="text-center text-light bg-dark"), body=True, color="dark")
        , className="mt-4 mb-4")
    ]),
    # dbc.Row([
    #     dbc.Col(html.H5(children='Latest update: 7 June 2020', className="text-center"),
    #                      width=4, className="mt-4"),
    #     # dbc.Col(html.H5(children='Daily figures since 31 Dec 2019', className="text-center"), width=8, className="mt-4"),
    #     ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='st_cases')),
        # dbc.Col(dcc.Graph(id='line_cases_or_deaths'), width=6)
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Total Deaths in India: ',id="st_lab2",
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='st_deaths')),
    ]),

        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Total Cured in India: ', id="st_lab3",
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(dcc.Graph(id='st_cured')),
        ]),

    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='Figures by States Comparison',
                                 className="text-center text-light bg-dark"), body=True, color="dark")
        , className="mb-4")
        ]),
    # html.Div([
    #     html.Div([
    #     dbc.Row([
        html.Div([
            dcc.Dropdown(
            # html.Div([
            id='sts',
            options=[{'label': i, 'value': i} for i in available_states],
            value=['Andhra Pradesh', 'Telengana'],
            multi=True)
            ],style={'width': '50%', 'margin-left': '5px',"padding":10}),
            # )],
    dcc.Dropdown(
            id='cols',
            options=[{'label': i, 'value': i} for i in avail_col],
            value='Confirmed',
            # multi=True,
            style={'width': '70%', 'margin-left': '5px'}),
        # )],
    dbc.Row([
        dbc.Col(html.H5(children='Density Figure', className="text-center"),
                className="mt-4"),
    ]),


    dcc.Graph(id='den'),

    dbc.Row([
        dbc.Col(html.H5(children='Cumulative Figures of All States in India', className="text-center"),
                className="mt-4"),
    ]),

    dcc.Graph(id='cum'),

])


])
@app.callback(
Output("st_lab","children"),
    [Input("state","value")]
)
def total_cases(count):
    df1 = df.loc[(df['State/UnionTerritory'] == count)]
    last_row = df1.iloc[[-1]]
    value = int(last_row['Confirmed'])
    return "Total cases in {} are  :  {}".format(count, value)


@app.callback(
Output("st_lab2","children"),
    [Input("state","value")]
)
def total_cases(count1):
    df1 = df.loc[(df['State/UnionTerritory'] == count1)]
    last_row = df1.iloc[[-1]]
    value = int(last_row['Deaths'])
    return "Total Deaths in {} are  :  {}".format(count1, value)

@app.callback(
Output("st_lab3","children"),
    [Input("state","value")]
)
def total_cases(count1):
    df1 = df.loc[(df['State/UnionTerritory'] == count1)]
    last_row = df1.iloc[[-1]]
    value = int(last_row['Cured'])
    return "Total Cured in {} are  :  {}".format(count1, value)

@app.callback(
    Output("st_cases","figure"),
    [Input("state","value")]
)
def figure_case(count2):
    df2 = df.loc[(df['State/UnionTerritory'] == count2)]
    return px.area(
        df2, x="Date", y="Confirmed", color="State/UnionTerritory", line_group="State/UnionTerritory"
    )

@app.callback(
    Output("st_deaths","figure"),
    [Input("state","value")]
)
def figure_deaths(count3):
    df2 = df.loc[(df['State/UnionTerritory'] == count3)]
    return px.area(
        df2, x="Date", y="Deaths", color="State/UnionTerritory", line_group="State/UnionTerritory"
    )

@app.callback(
    Output("st_cured","figure"),
    [Input("state","value")]
)
def figure_deaths(count3):
    df2 = df.loc[(df['State/UnionTerritory'] == count3)]
    return px.area(
        df2, x="Date", y="Cured", color="State/UnionTerritory", line_group="State/UnionTerritory"
    )

@app.callback(
Output("den","figure"),
    [Input("sts","value"), Input("cols","value")]
)
def density_fig(ch1, ch2):
    df3 = df.loc[df["State/UnionTerritory"].isin(ch1)]

    return px.area(
        df3, x="Date", y=ch2, color="State/UnionTerritory", line_group="State/UnionTerritory"
    )

@app.callback(
Output("cum","figure"),
    [Input("cols","value")]
)
def line_fig(ch2):
    # df3 = df.loc[df["State/UnionTerritory"].isin(ch1)]
    return px.line(
        df, x="Date", y=ch2, color="State/UnionTerritory",labels="State/UnionTerritory"
    )
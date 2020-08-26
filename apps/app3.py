# import plotly.graph_objects as go
import pandas as pd
from data_files import data
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
df = pd.read_csv(data, index_col = 0)

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
available_countries = df['location'].unique()
avail_col = df.columns
# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='COVID-19 World Dashboard'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Visualising COVID-19 World Data'), className="mb-4")
        ]),
# choose between cases or deaths
    dcc.Dropdown(
        id='count',
        options=[
            {'label': "World", 'value': "World"}
        ],
        value='World',
        #multi=True,
        style={'width': '50%'}
        ),
# for some reason, font colour remains black if using the color option
    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='Total Cases in World',id="wr1",
                                 className="text-center text-light bg-dark"), body=True, color="dark")
        , className="mt-4 mb-4")
    ]),
    # dbc.Row([
    #     dbc.Col(html.H5(children='Latest update: 7 June 2020', className="text-center"),
    #                      width=4, className="mt-4"),
    #     # dbc.Col(html.H5(children='Daily figures since 31 Dec 2019', className="text-center"), width=8, className="mt-4"),
    #     ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='cases1')),
        # dbc.Col(dcc.Graph(id='line_cases_or_deaths'), width=6)
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Total Deaths in World: ',id="wr2",
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ]),
        # dbc.Row([
        #     dbc.Col(html.H5(children='Latest update: 7 June 2020', className="text-center"),
        #             width=4, className="mt-4"),
        #     dbc.Col(html.H5(children='Cumulative figures since 31 Dec 2019', className="text-center"), width=8,
        #             className="mt-4"),
        # ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='deaths1')),
        # dbc.Col(dcc.Graph(id='total_line_cases_or_deaths'), width=8)
    ]),
    #
    # dbc.Row([
    #     dbc.Col(dbc.Card(html.H3(children='Figures by Country Comparison',
    #                              className="text-center text-light bg-dark"), body=True, color="dark")
    #     , className="mb-4")
    #     ]),
    # html.Div([
    #     html.Div([
    #     dbc.Row([
    #     html.Div([
    #         dcc.Dropdown(
    #         # html.Div([
    #         id='countries',
    #         options=[{'label': i, 'value': i} for i in available_countries],
    #         value=['Afghanistan', 'India'],
    #         multi=True)
    #         ],style={'width': '50%', 'margin-left': '5px',"padding":10}),
    #         # )],
    # dcc.Dropdown(
    #         id='columns',
    #         options=[{'label': i, 'value': i} for i in avail_col],
    #         value='total_cases',
    #         # multi=True,
    #         style={'width': '70%', 'margin-left': '5px'}),
    #     # )],
    # dbc.Row([
    #     dbc.Col(html.H5(children='Density Figures', className="text-center"),
    #             className="mt-4"),
    # ]),
    #
    #
    # dcc.Graph(id='cases_or_deaths_country'),
    #
    # dbc.Row([
    #     dbc.Col(html.H5(children='Cumulative Figures', className="text-center"),
    #             className="mt-4"),
    # ]),
    #
    # dcc.Graph(id='total_cases_or_deaths_country'),

])


])
@app.callback(
Output("wr1","children"),
 [Input("count","value")]
)
def total_cases(c):
    # count = "World"
    df1 = df.loc[(df['location'] == c)]
    last_row = df1.iloc[[-1]]
    value = int(last_row['total_cases'])
    return "Total cases in {} are  :  {}".format(c, value)


@app.callback(
Output("wr2","children"),
    [Input("count", "value")]

)
def total_cases(c1):
    df1 = df.loc[(df['location'] == c1)]
    last_row = df1.iloc[[-1]]
    value = int(last_row['total_deaths'])
    return "Total Deaths in {} are  :  {}".format(c1, value)

@app.callback(
    Output("cases1","figure"),
    [Input("count", "value")]

)
def figure_case(c2):
    # count2 = "World"
    df2 = df.loc[(df['location'] == c2)]
    return px.area(
        df2, x="date", y="total_cases", color="location", line_group="location"
    )


@app.callback(
    Output("deaths1","figure"),
    [Input("count", "value")]

)
def figure_deaths(count3):
    # count3 = "World"
    df2 = df.loc[(df['location'] == count3)]
    return px.area(
        df2, x="date", y="total_deaths", color="location", line_group="location"
    )
#
# @app.callback(
# Output("cases_or_deaths_country","figure"),
#     [Input("countries","value"), Input("columns","value")]
# )
# def density_fig(ch1, ch2):
#     df3 = df.loc[df["location"].isin(ch1)]
#     return px.area(
#         df3, x="date", y=ch2, color="location", line_group="location"
#     )
#
# @app.callback(
# Output("total_cases_or_deaths_country","figure"),
#     [Input("countries","value"), Input("columns","value")]
# )
# def line_fig(ch1, ch2):
#     df3 = df.loc[df["location"].isin(ch1)]
#     return px.line(
#         df3, x="date", y=ch2, color="location", line_group="location"
#     )
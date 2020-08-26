# import pandas as pd
import csv
from data_files import india_data
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly_express as px
from app import app


layout = html.Div([
    dbc.Container([
        dcc.Location(id="url",refresh=True),
        dbc.Row([
            dbc.Col(html.H1(children='Feedback and Report Bugs:'), className="text-center")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Report any Bugs or Send some feedback of the COVID-19 Dashboard!'), className="text-center")
        ],style={"marginBottom":"30px"}),
        dbc.Row([
            dbc.Col(
        dcc.Input(id="input1",type="text",placeholder="Enter your name:",size="40"), className="text-center"
            )

        ],style={"marginBottom":"30px"}),
        dbc.Row([
            # dbc.Col(
            dcc.Textarea(
                    id='textarea-state-example',
                    value='',
                    style={'width': '100%', 'height': 200},
                ),
                html.Button('Submit', id='textarea-state-example-button', n_clicks=0, className="text-center"),
                html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line'})

            # )
        ], style={"marginBottom":"30px"}),
        # dbc.Row([
        #     html.H5(id="out")
        # ])

    ])
    ])

@app.callback(
    Output('url', 'pathname'),
    [Input('textarea-state-example-button', 'n_clicks'), Input("input1","value"), Input('textarea-state-example', 'value')],
    # [State('textarea-state-example', 'value')]
)
def update_output(n_clicks, name, feedback):
    outfile = open('data_files/fed_back.csv', 'a', newline='')
    w = csv.writer(outfile)

    name_data = name
    feedback_data = feedback

    if n_clicks > 0:
        w.writerow([name_data, feedback_data])
        return "/report"
import pandas as pd
from data_files import india_data
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly_express as px
from app import app


layout = html.Div([
    html.Div([
    # html.Img(s    rc="assets/ok.jpg")
    # ],style={"marginBottom":"1000px"}),
    dbc.Container([
# html.Div(
#    html.Div(html.H6('here is some text')),
#    html.Div(html.Img(src="me2.png")),style={"display":"inline-block", "height":'200px'}
# )
        html.Div([
        dbc.Row([
            html.Div([
            dbc.Col(
                html.H1(children='about me',style={"font-family":"Alata", "font-size":90})
                )

        ],style={"marginBottom":"30px"})
        ]),

        dbc.Row([
            html.Div([
            dbc.Col(
                dcc.Markdown('''
                ## Hello, everyone I'm Siddharth Pilli, and I'm 12 years old,
                ## and currently I work as a Data-scientist.

                '''),style={"font-family":"Alata"}
            )
                ], style={"marginBottom":"30px"})
        ]),
        dbc.Row([
            html.Div([
            dbc.Col(
                dcc.Markdown('''
                ### I've created this Web-Application Dashboard, mainly focusing,
                ### for Indian regions so every Indian can know how COVID-19 is
                ### affecting our lives!

                '''), style={"font-family": "Alata"}
            )
                ], style={"marginBottom":"30px"})
        ]),
        dbc.Row([
            html.Div([
            dbc.Col(
             html.A("You all can find me on LinkedIn", href="https://www.linkedin.com/in/siddharth-pilli-a55616169/",style={"font-family":"Alata"})
            )
                ], style={"marginBottom":"10px"})
        ]),
        dbc.Row([
            html.Div([
                dbc.Col(
                    html.A("You all can find me on Facebook also",
                           href="https://www.facebook.com/siddharth.pilli.1",
                           style={"font-family": "Alata"})
                )
            ], style={"marginBottom": "3px"})
        ]),
        # dbc.Row([


        ]),
        #
        # html.Div()
        # html.Img(src="me2.png")
        # html.Div([
        #     html.Img(src='assets/me2.png')
        # ], style={"display":"inline-block"}),

        # html.Div([
        # ])
    ]),
        # dbc.Container([
        html.Div([
    html.Img(src="assets/me.png",style={'margin-right':"-150px",'margin-left':"auto","display":"block","margin-top":"-380px","height":"450px"})
            ])
            # ])
    ])])

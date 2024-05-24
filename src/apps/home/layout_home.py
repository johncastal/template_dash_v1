from dash import html
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
from dash import dash_table



layout = html.Div(
    children=[

        html.H1("Hello world"),
        html.P("This is my first app in dash"),

    ], className='container'
)

import dash_bootstrap_components as dbc
import dash


app = dash.Dash(external_stylesheets=[dbc.themes.SIMPLEX], 
                title='My first app in Dash', 
                suppress_callback_exceptions=True,
                meta_tags=[{'name':'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

server = app.server
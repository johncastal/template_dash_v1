from dash.dependencies import Input, Output, State
from flask_caching import Cache
from dash import html
import dash_bootstrap_components as dbc
from dash import html, Input, Output
from dash.exceptions import PreventUpdate



#main dash instance
from app import app

#call modules needed for callbacks
from apps.home import layout_home



#cache configuration
TIMEOUT = 240
cache = Cache(app.server, config={
    'CACHE_TYPE':'filesystem',
    'CACHE_DIR': 'cache-directory',
    'CACHE_THRESHOLD': 20
})

#Entire callbacks definition
def register_callbacks(app):
    #callback for navigation, look for url and respond with the right layout
    @cache.memoize(timeout=TIMEOUT)
    @app.callback(Output("page-content", "children"),[Input("url","pathname")])
    def render_page_content(pathname):
        if pathname in ["/","/apps/home/layout_home"]:
            return layout_home.layout
        #elif pathname in ["/","/apps/form/layout_main"]:
        #    return layout_1.layout


        #If the user tries to reach a different page, return a 404 message
        left_jumbotron = dbc.Col([
            html.Div(
                [
                    html.H2("404: Not Found", className="display-3"),
                    html.Hr(className="my-2"),
                    html.P(
                        f"The pathname {pathname} was not recognised..."
                    ),
                    html.H1(["",html.Br()]),
                    html.H1(["",html.Br()]),
                    html.H1(["",html.Br()]),
                    html.H1(["",html.Br()]),
                    html.H1(["",html.Br()]),
                    html.H1(["",html.Br()]),
                    #dbc.Button("Example Button", color="light", outline=True),
                ],
                className="E404 h-100 p-5 text-white bg-dark rounded-3",
            ),
            #md=6,
        ],lg='12',md=6)
        return left_jumbotron


### STARTING CALLBACKS ###

# Callback 1
@app.callback(
    #Output('Datos_actualizados', 'children'),
    Output('output', 'children'),
    Input('input', 'n_clicks'),

)
def update_output(n_clicks):

    if n_clicks>0:
        print("test")
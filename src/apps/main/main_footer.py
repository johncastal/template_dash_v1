from dash import html
import dash_bootstrap_components as dbc


layout = html.Div([
    html.Div([
        html.Div([
            html.H3("Alcance:"),
            html.A([
                html.P("""Aplicación de datos desarrollada para...""")
            ]),
        ],className="footer_alc"),
        html.Div([
            html.H3("Desarrollado por: "),
                html.A([
                    html.P("XXXXXXXXXXXXXXX")
                ], #href="#"
                )
            ],className="footer_dev"),
        ],className="footer_size"),
],className="footer")
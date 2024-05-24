import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State
from dash import html, Input, Output

from app import app


LOGO = "\\assets\Logo_CHEC.png"

menu_bar = [
    dbc.NavItem(
        dbc.NavLink("NavLink", active = True, href = "/apps/home/layout_home", class_name="page-link_active")),
    dbc.NavItem(
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("DropdownMenu1", href = "/apps/#/#"), dbc.DropdownMenuItem("DropdownMenu2", href = "/apps/#/#")],
            label="Test Menu",
            nav=True,
        ),
    ),
]

navbar = dbc.Navbar(
    [

        html.A([
                html.Img(src=LOGO, id='logo'),
            ],
            #href="//chec-app33:8052/", 
            style={"textDecoration":"none"},
            className="brand"
            ),

        html.H1("Aplicación de datos", className='navbar-titulo'),

        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        dbc.Collapse(
            menu_bar,
            id="navbar-collapse", 
            navbar=True, 
            is_open=False
        ),
    ],
    #color="light",
    #dark=True,
    className = "navbar",
)

layout = html.Div(
    [
        navbar
    ],
    id="menu",
)

#add callback for toggling the collapse on small screens 
#@app.callback(
#    Output("navbar-collapse","is_open"),
#    [Input("navbar-toggler", "n_clicks")],
#    [State("navbar-collapse", "is_open")],
#)
#def toggle_navbar_collapse(n,is_open):
#    if n:
#        return not is_open
#    return is_open
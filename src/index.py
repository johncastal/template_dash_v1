from dash import dcc
from dash import html
import os
#import dash_auth

#Organizar directorio principal multiplataforma
currDir = os.getcwd()
verifDir = currDir.find('src')
if verifDir>0:
    mainDir = os.getcwd()
    os.chdir(mainDir)
else:
    mainDir = os.getcwd() + '/src'
    os.chdir(mainDir)
#callbacks import
from callbacks import register_callbacks

#dash instance
from app import app

#dash custom modules
from apps.main import main_nav, main_content, main_footer

#basic auth definition
#USERNAMEINFO = [['user', 'password']]
#auth = dash_auth.BasicAuth(app,USERNAMEINFO)

#Example first layout
#app.layout = html.Div([
#    html.H1("Hello world"),
#    html.P("This is my first app in dash")
#])

#main layout
app.layout = html.Div(className='wrapper',
    children=[
        dcc.Location(id='url', refresh=False),
        main_nav.layout,
        main_content.layout,
        main_footer.layout
    ]
)

#callbacks register
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
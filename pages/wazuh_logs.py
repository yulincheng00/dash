from dash import html
import dash_bootstrap_components as dbc
from dash import dcc, html, callback

STYLE = {
    "transition": "margin-left .5s",
    "margin-top": "2rem",
    "margin-left": "15rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "position":"relative",
    "left":'0.2rem',
    "width":"73rem",
    "background-color": "#f8f9fa",
    'fontSize': 30,
    'zIndex':1,
}
dropdown_style = {
    "display":"inline-block",
    "fontSize":30,
    "width":'300px',
    "height":"100px",
    "position":"relative",
    "left":"1rem",
    "top":"2rem"
}

def serve_layout():
    layout = html.Div(
        [
            html.P("Welcome to wazuh logs"),
            dbc.Row(
                    dbc.Col(
                        html.Div(children=[
                        dcc.Dropdown(                       
                            id="choice_agent",
                            options=[
                                {'label': 'Agent_A'},
                                {'label': 'Respberry_pi'}
                            ],
                            placeholder="agent",
                        )
                        ],style=dropdown_style),
                    )
            ),
        ],
        style=STYLE,
    )
    return layout

import dash_bootstrap_components as dbc
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State, ALL
import feffery_antd_components as fac
import pandas as pd
from dash import Dash, dash_table

from process_time import process_time
from components import log_display

# components
# hitNum = html.H1(
#     [
#         '載入資料中',
#         dbc.Spinner(size="lg", spinner_style={'margin-left': '15px', 'width': '40px', 'height': '40px'}),
#     ],
#     style={'textAlign': 'center'}, id='dataNum'
# )


dropdown_style = {
    "display":"inline-block",
    "fontSize":20,
    'width': '200px',
    "position":"relative",
    "left":"1rem",
    "top":"1rem",
    "bottom":"2rem"
}

STYLE = {
    "transition": "margin-left .5s",
    "margin-top": "2rem",
    "margin-left": "15rem",
    "margin-right": "1rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    'fontSize': 30,
    'zIndex':1,
    # 'border':'1px black solid',
    "position":"relative",
    "left":"0.5rem",
    "top":"1rem"
}



def serve_layout():
    df = pd.read_csv('./example.csv')
    table = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
    layout = html.Div(
        [
            html.P("Welcome to Suricata logs"),
            dbc.Row(
                fac.AntdSelect(
                    placeholder='Agent:',
                    options=[
                        {'label': 'Raspberry Pi', 'value': 'Raspberry Pi'},
                        {'label': 'PC', 'value': 'PC'},
                    ],
                    style=dropdown_style
                ),
            ),
            dbc.Row(
                html.Div(
                    [
                        html.P("welcome"),
                        table
                    ],
                ),
            ),
            
        ],
        style=STYLE,
    )
    return layout
# @callback(
#     [
#         Output("log-table", "children"),
#     ],
#     [
#         Input("table-update", 'n_interval'),
#     ],
# )

# def update(n_clicks, add_btn, del_btns, time):
#     # 將 time 轉成 timestamp format, 並得到 interval
#     currentDate, freqs = process_time.get_time_info(time)
#     return log_display.update(currentDate, freqs)

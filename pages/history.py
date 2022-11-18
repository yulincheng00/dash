import dash_bootstrap_components as dbc
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State, ALL
import feffery_antd_components as fac
from process_time import process_time
import dash
import globals
from components import fields, datePicker, history_display, collapse_item, alert
dropdown_style = {
    "display":"inline-block",
    "fontSize":20,
    'width': '200px',
    "position":"relative",
    "left":"1rem",
    "top":"1rem",
    "bottom":"2rem"
}
# components
hitNum = html.H1(
    [
        '載入資料中',
        dbc.Spinner(size="lg", spinner_style={'margin-left': '15px', 'width': '40px', 'height': '40px'}),
    ],
    style={'textAlign': 'center'}, id='hdataNum'
)

DISPLAY_STYLE = {
    "transition": "margin-left .5s",
    "margin-top": 20,
    "margin-right": 30,
    "padding": "1rem 1rem",
    "background-color": "#f8f9fa",
    'fontSize': 12,
    # 'border':'1px black solid',
    'width': '1px',
    'zIndex':1,
}

def serve_layout():
    # first, notification = alert.update_notification(first)

    layout = html.Div(
        [
            dbc.Row(
                [
                    fields.serve_fields(),

                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    datePicker.his_date_picker(),   # live update
                                    # notification #,style={'margin-right':'3rem'}
                                ],
                            ),
                            fac.AntdSelect(
                                id = 'hisagentselect',
                                placeholder='Agent:',
                                options=[
                                    {'label': 'Raspberry Pi', 'value': 'Raspberry Pi'},
                                    {'label': 'PC', 'value': 'PC'},
                                ],
                                style=dropdown_style
                            ),
                            
                            dcc.Loading(
                                html.Div(
                                    [
                                        hitNum,
                                        dbc.Col(id='hgraph-and-table'),
                                    ],
                                ),
                            ),
                        ],
                        style=DISPLAY_STYLE,
                    ),
                ],
            ),
        ],
    )
    return layout

# 初始化 display or 按下 Update 按鈕的觸發事件 or 利用 fields_btn 來動態 update display
@callback(
    [
        Output('hdatetime-output', 'children'),
        Output('hdataNum', 'children'),
        Output("hgraph-and-table", "children"),
    ],
    [
        Input('submit_date', 'n_clicks'),
        Input({'type': 'add_btn', 'index': ALL}, 'n_clicks'),
        Input({'type': 'del_btn', 'index': ALL}, 'n_clicks'),
        Input('hisagentselect', 'value'),
    ],
    [
        State('hdatetime-picker', 'value'),
    ]
)
def update(n_clicks, add_btn, del_btns, value, time): #,dagentselect
    # 將 time 轉成 timestamp format, 並得到 interval
    startDate, endDate, freqs = process_time.get_time_info(time)
    if(value=='Raspberry Pi'):
        return history_display.update(startDate, endDate, freqs, globals.agent_pi_id)
    elif(value=='PC'):
        return history_display.update(startDate, endDate, freqs, globals.agent_pc_id)
    return dash.no_update, dash.no_update, dash.no_update
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc, html, callback, dash_table
import pandas as pd
import json
from pandas import json_normalize
import globals
from components import hids_logtojson
from datetime import date

table_style = {
    "margin-left": "1rem",
    "margin-right": "1rem",
    "position":"relative",
    "left":"0.5rem",
    "top":"2rem",
    'fontsize':12,
}


# global CONFIG

def update(id):
    print(id)
    today = date.today()
    todate = today.strftime("%m/%d/%y")
    #在server上需要取消註解這行 ： hids_logtojson.log2json(globals.hidsdirpath+'/2022/Aug/ossec-alerts-09.json')
    #讀取json檔, 篩選今天的log內容
    global df, df_
    df = pd.read_json(open(globals.hidsdirpath+'/2022/Aug/ossec-alerts-09.json', "r", encoding="utf8"))
    #在server上需要改 ： open(globals.hidsdirpath+'/'+today.year+'/'+today.strftime("%b")+'/ossec-alerts-'+today.day+'.json'
    df = df.loc[:, ["timestamp", "rule", "agent"]]
    df_=pd.DataFrame()
    df_['Date'] = df['timestamp'].apply(lambda x: x.strftime("%Y/%m/%d"))
    df_['Time'] = df['timestamp'].apply(lambda x: x.strftime("%H:%M:%S"))
    df_['Agent_ID'] = df['agent'].apply(lambda x: x['id'])
    df_['Agent'] = df['agent'].apply(lambda x: x['name'])
    df_['Event'] = df['rule'].apply(lambda x: x['description'])
    df_['Level'] = df['rule'].apply(lambda x: x['level'])

    del df
    df = df_
    df = df[((df['Date'] == '2022/08/09') & (df['Agent_ID'] == id))]
    all_cols = list(df.columns)

    table = dash_table.DataTable(
        virtualization=True,
        data=df.to_dict('records'),
        columns=[{'name': column, 'id': column} for column in all_cols],
        # fixed_columns={ 'headers': True, 'data': 1},
        style_header={
            'backgroundColor': '#99ABBD',
            'color': 'black',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'border':'1px black solid',
        },
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
        },
        style_cell={
            # all three widths are needed
            'width': '180px',
            # 'overflow': 'hidden',
            # 'textOverflow': 'ellipsis',
            'textAlign': 'center',
            'fontsize':12,
            'height': 'auto',

        },
        style_table={
            'minWidth': '100%',
            'Width': '100%'
        },
    )

    # # default_page_size = 100 # 每頁預設 data 數
    # display = [
    #     html.Br(),
    #     table,
    # ],style = table_style

    return table

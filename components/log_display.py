# import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output
# from dash import dcc, html, callback, dash_table

# import globals
# from plot import table
# from components.se_display import CONFIG


# # global CONFIG

# def update(currentDate, freqs):
#     global CONFIG

#     # 根據 selected_fields 篩選資料(若 fields 為空, table 顯示所有 fields)
#     global df
#     df= table.update(currentDate, freqs)

#     all_cols = list(df.columns)

#     # 解決 data table 中 list 的顯示問題, 將 df 中的 list 轉成 string 用逗號隔開, 並串接在一起
#     for column in all_cols:
#         df[column] = [', '.join(map(str, l)) if isinstance (l, list) else l for l in df[column]]

#     # 根據 column 名稱長度, 自動調整 data table 的 header 寬度
#     long_column_names = [{"if": {"column_id": column}, "min-width": "300px"} for column in all_cols if len(column) >= 30]
#     med_column_names = [{"if": {"column_id": column}, "min-width": "225px"} for column in all_cols if (len(column) > 15 and len(column)) < 30]
#     small_column_names = [{"if": {"column_id": column}, "min-width": "120px"} for column in all_cols if len(column) <= 15]

#     adjusted_columns = long_column_names + med_column_names + small_column_names

#     table = dash_table.DataTable(
#         data=df.to_dict('records'),
#         columns=[{'name': column, 'id': column} for column in all_cols],
#         virtualization=True,
#         sort_action='custom',
#         sort_mode='multi',
#         # 要 minWidth, maxWidth 同時設一樣, 再搭配 fixed_rows, 才能 fixed header
#         style_cell={
#             'textAlign': 'center',
#             # 'overflow': 'hidden',
#             # 'textOverflow': 'ellipsis',
#             'minWidth': 240,
#             'maxWidth': 240,
#             'whiteSpace': 'pre-line',   # 超過自動換行
#         },
#         fixed_rows={
#             'headers': True,
#             'data': 0,
#         },
#         style_cell_conditional=adjusted_columns,
#         # filter_action="native",
#         style_header={
#             'backgroundColor': '#99BDBB',
#             'color': 'black',
#             'fontWeight': 'bold',
#             'textAlign': 'center',
#             'minWidth': '100%',
#         },
#         tooltip_data=[
#             {
#                 column: {'value': f'{value}', 'type': 'markdown'}
#                 for column, value in row.items()
#             } for row in df.to_dict('records')
#         ],
#         tooltip_header={i: i for i in all_cols},
#         id='dash-table',
#         page_action='custom',   # 後端分頁
#         page_current=0,
#         page_size=100,
#         tooltip_delay=0,
#         tooltip_duration=None
#     )

#     default_page_size = 10 # 每頁預設 data 數
#     display = [
#         html.Br(),
#         table,
#     ]

#     return [f'{currentDate}', f'{len(df)} hits', display]

# # 後端分頁, 以減少延遲和內存壓力, 外加排序功能
# @callback(
#     [
#         Output('dash-table', 'data'),
#         Output('dash-table', 'page_count'),
#         Output('dash-table', 'tooltip_data'),
#         Output('page-size', 'children'),
#     ],
#     [
#         Input('dash-table', 'page_current'),
#         Input('dash-table', 'page_size'),
#         Input('dash-table', 'sort_by'),
#         Input('row_drop', 'value'),
#     ]
# )
# def refresh_page_data(page_current, page_size, sort_by, value):
#     global df
#     page_size = value

#     # sort_by 紀錄參與排序的 col_name, 以及其排序方式(asc, desc)
#     if sort_by:
#         df = df.sort_values(
#             [col['column_id'] for col in sort_by],
#             ascending=[
#                 col['direction'] == 'asc'
#                 for col in sort_by
#             ]
#         )

#     return [
#         df.iloc[page_current * page_size:(page_current + 1) * page_size].to_dict('records'),
#         1 + df.shape[0] // page_size,
#         [
#             {
#                 column: {'value': f'{value}', 'type': 'markdown'}
#                 for column, value in row.items()
#             } for row in df.iloc[page_current * page_size:(page_current + 1) * page_size].to_dict('records')
#         ],
#         f'每頁{page_size}筆'
#     ]
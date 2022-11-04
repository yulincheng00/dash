# import pandas as pd
# import plotly.express as px

# from plot import donut
# from database import get_db
# from process_time import process_time

# def update(currentDate, freqs):
#     # connect to database
#     posts = get_db.connect_db()

#     # 根據 interval 切割 startDate ~ endDate
#     intervals = list(pd.date_range(currentDate, currentDate, freq=freqs))

#     # 轉成 timestamp 格式
#     intervals = process_time.timestamp_format(intervals, currentDate)

#     #Suricata log
#     display_cols = {'Time', 'alert.signature', 'src_ip', 'src_port', 'dest_ip', 'dest_port'}
    
#     # 計算 interval 中的 data 個數
#     cnt = []
#     for i in range(1, len(intervals[:-1])):
#         result = posts.count_documents({'$and':[{'timestamp':{"$gte":intervals[i-1]}},
#                                                 {'timestamp':{"$lt":intervals[i]}}]})
#         cnt.append(result)


#     # 找到 startDate ~ endDate 之間的所有 data, 並轉成 data table 的形式
#     data = posts.find({'timestamp':{"$eq":currentDate}}, display_cols)
#     df = pd.json_normalize(data)

#     # 若 selected_fields 有 field 沒出現在 df 中 (代表該 field 在 query 後全為空值, 所以沒出現在 df 中)
#     df_columns = list(df.columns)
#     empty_col = ['-' for i in range(len(df))]

#     # 用 - 取代 df 中的空值
#     df.fillna('-', inplace=True)

#     interval_title = process_time.interval_title
#     data = {'time':intervals[:-1]}
#     data['Count'] = cnt

#     return df
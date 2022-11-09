import pandas as pd
import ast
import json

# f = open('/home/ne6101157/wazuh_data/2022/Aug/ossec-alerts-09.json',"r")
# Lines = f.readlines()
# jsons=[]
# count = 0
# # 轉換成正常JSON格式
# for line in Lines:
#     print(type(line))
#     count += 1
#     if "false" in line:
#         line = line.replace('false', "'false'")
#     if "true" in line:
#         line = line.replace('true', "'true'")
#     json_data = ast.literal_eval(line)
#     jsons.append(json_data)
#     print(json_data)
# print(jsons)

# with open("/home/ne6101157/wazuh_data/2022/Aug/ossec-alerts-09.json", "w") as f:
#     json.dump(jsons, f, indent = 4)

#提取特徵
global df
df = pd.read_json(open("/home/ne6101157/wazuh_data/2022/Aug/ossec-alerts-09.json", "r", encoding="utf8"))
df = df.loc[:, ["timestamp", "rule", "agent"]]
print(df.iloc[0])
df_=pd.DataFrame()
df_['Date'] = df['timestamp'].apply(lambda x: x.strftime("%Y/%m/%d"))
df_['Time'] = df['timestamp'].apply(lambda x: x.strftime("%H:%M:%S"))
df_['Agent'] = df['agent'].apply(lambda x: x['name'])
df_['Event'] = df['rule'].apply(lambda x: x['description'])
df_['Level'] = df['rule'].apply(lambda x: x['level'])

print(df_)
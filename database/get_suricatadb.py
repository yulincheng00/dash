# import os
# from pymongo import MongoClient
# import glob
# import json
# from database import create_db, update_suricatadb, del_db

# def get_current_db(dir_path, sudoPassword):
#     # 當 last_date.pkl 不存在時(更新版本), 刪除 DB 
#     if not os.path.isfile('./last_date.pkl'):
#         del_db.delete()

#     client = MongoClient()
#     suricatadb = client['suricatadb']
#     current_db = suricatadb.list_collection_names(include_system_collections=False)
#     posts = suricatadb.posts

#     if suricatadb == []:
#         num = 0
#         data = []
#         error_file = ''
#         json_files = []
#         f = open('fast.json', 'r')
#         try:
#             posts.insert_many(data) # insert data into mongoDB
#         except:
#             print(f'重新 insert {error_file}')
#             f = open(error_file, 'r')
#             lines = f.readlines()
#             json_lines = [json.loads(line) for line in lines]
#             num += len(lines)
#             posts.insert_many(json_lines)
#         return num
#     else:
#         num = update_suricatadb.update_db(posts, dir_path, sudoPassword)
#     return client, posts, num, current_db

# def connect_db():
#     client = MongoClient()
#     suricatadb = client['suricatadb']
#     posts = suricatadb.posts
#     return posts
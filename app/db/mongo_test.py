import datetime
from pymongo import MongoClient

# mongod --dbpath ./db/mongodb を実行する

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
  'name': 'customer1',
  'pip': ['python', 'java', 'go'],
  'info': {'os': 'mac'},
  'date': datetime.datetime.now(datetime.timezone.utc)
}

stack2 = {
  'name': 'customer2',
  'pip': ['python', 'java'],
  'info': {'os': 'windows'},
  'date': datetime.datetime.now(datetime.timezone.utc)
}

# データを登録
db_stacks = db.stacks
# stack_id = db_stacks.insert_one(stack1).inserted_id
# print(stack_id, type(stack_id))
# print('############')
# print(db_stacks.find_one({'_id': stack_id}))

# ObjectIdからデータを取得
# from bson.objectid import ObjectId
# str_stack_id = '66d3db6ffa8597867dcb0e4a'
# print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))

# 値を指定して取得
# db_stacks.find_one({'name': 'customer1'})

# stack_id = db_stacks.insert_one(stack2).inserted_id
# print(stack_id, type(stack_id))

# 全て取得してforループで表示
# for stack in db_stacks.find():
#     print(stack)

# 現在の時間よりも前に登録されたデータを一覧取得
# now = datetime.datetime.now(datetime.timezone.utc)
# for stack in db_stacks.find({'date': {'$lt': now}}):
#     print(stack)
    
# シンプルなデータ構造であればmongodbが選択される。（ログとして使用するなど）

# データを更新
# db_stacks.find_one_and_update(
#     {'name': 'customer1'}, {'$set': {'name': 'YYY'}}
# )
# print(db_stacks.find_one({'name': 'YYY'}))

# データを削除
# db_stacks.delete_one({'name': 'YYY'})
# print(db_stacks.find_one({'name': 'YYY'}))

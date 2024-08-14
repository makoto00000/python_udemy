import datetime

now = datetime.datetime.now()
print(now) # 2024-08-12 05:15:15.625960
print(now.isoformat()) # 2024-08-12T05:15:54.919110
print(now.strftime('%d/%m/%y-%H:%M:%S:%f')) # 12/08/24-05:17:20:809009

today = datetime.date.today()
print(today) # 2024-08-12
print(today.isoformat()) # 2024-08-12
print(now.strftime('%d/%m/%y')) # 12/08/24

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t) # 01:10:05.000100
print(t.isoformat()) # 01:10:05.000100
print(t.strftime('%H_%M_%S_%f')) # 01_10_05_000100

print(now) # 2024-08-12 05:22:46.568732
d = datetime.timedelta(weeks=1) 
print(now - d) # 2024-08-05 05:22:46.568732

import time
print('######')
# time.sleep(2)
print('######')

# エポックタイム（1970年1月1日からの秒数）
print(time.time()) # 1723440266.2887018


# ファイルのバックアップを作成する例
import os
import shutil

file_name = './file/test.txt'
if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')
    )) # 2024_08_12_05_28_24 が作成される
with open(file_name, 'w') as f:
    f.write('test')
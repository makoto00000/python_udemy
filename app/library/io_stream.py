import io
import requests
# import zipfile
import tarfile

# with open('/tmp/a.txt', 'w') as f:
#     f.write('test')

# with open('/tmp/a.txt', 'r') as f:
#     print(f.read())

# メモリ上で一時的に読み書きして、プログラム終了時には消去する

f = io.StringIO()  # string型
# f = io.BytesIO()  # byte型
f.write('string io test')
# f.write(b'string io test')
f.seek(0)
print(f.read())


url = ('https://files.pythonhosted.org/packages/dd/31/'
       '1c0dc71cd947a5c48f18b0ff9d8fd3a0da0bad9fa63c36dfd9715676926d/'
       'zip-0.0.2.tar.gz')

f = io.BytesIO()

r = requests.get(url)
f.write(r.content)

f.seek(0)

with tarfile.open(fileobj=f, mode='r:gz') as tar:
    # 解凍したファイルを一覧表示
    # for member in tar.getmembers():
    #     print(member.name)
    with tar.extractfile('zip-0.0.2/LICENSE') as file:
        print(file.read().decode('utf-8'))

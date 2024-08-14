import tempfile

# 一時的にファイルを作成して削除
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 一時的にファイルを作成して残す
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# 一時的にディレクトリを作成して削除
with tempfile.TemporaryDirectory() as td:
    print(td)

# ディレクトリを作成して残す
temp_dir = tempfile.mkdtemp()
print(temp_dir)
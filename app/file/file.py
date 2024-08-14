# f = open('./file/test.txt', 'w')
# f.write('Test\n')
# print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
# f.close()

s = """\
AAA
BBB
CCC
DDD
"""
# with open('./file/test.txt', 'w') as f:
#     f.write(s)

with open('./file/test.txt', 'r') as f:
    # まとめて読み込む
    # print(f.read())
    # while True:
        # 1行ずつ読み込む
        # line = f.readline()
        # print(line, end='')

        # 2文字ずつ読み込む
        # chunk = 2
        # line = f.readline(chunk)
        # print(line)
        # if not line:
        #     break

    print(f.tell())
    print(f.read(1)) # A
    f.seek(5)
    print(f.read(1)) # B
    f.seek(14)
    print(f.read(1)) # D
    f.seek(15)
    print(f.read(1)) # 
    f.seek(5)
    # また最初に戻る
    print(f.read(1)) # B

print('#######')

# 存在しなければ新規作成して読み書きモード
# with open('./file/test.txt', 'w+') as f:
#     f.write(s)
#     f.seek(0)
#     print(f.read())

# 既存ファイルの読み書きモード（事前にファイルが存在しないとエラーになる）
with open('./file/test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)

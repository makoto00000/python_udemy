import zipfile
import glob

# test_dir/test.txtの構成でzipファイルが作成される
# with zipfile.ZipFile('./file/test.zip', 'w') as z:
#     z.write('./file/test_dir')
#     z.write('./file/test_dir/test.txt')

# 以下のコマンドで解答
# unzip test.zip -d zzz

# 上記の書き方だとディレクトリを一つずつ指定する必要があるので、全て読み込ませる。
with zipfile.ZipFile('./file/test.zip', 'w') as z:
    # *だけだと直下しかみない。**だと下までみる
    for f in glob.glob('./file/test_dir/**', recursive=True):
        # print(f)
        z.write(f)

# zipファイルの読み取り
with zipfile.ZipFile('./file/test.zip', 'r') as z:
    # zzzというファイル名で展開
    # z.extractall('zzz')
    with z.open('file/test_dir/test.txt') as f:
        print(f.read())

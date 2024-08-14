import tarfile

# ./file/test_dirをtest.tar.gzという名前で圧縮
with tarfile.open('./file/test.tar.gz', 'w:gz') as tr:
    tr.add('./file/test_dir')

# 以下のコマンドで展開
# tar zxvf test.tar.gz -C /tmp

with tarfile.open('./file/test.tar.gz', 'r:gz') as tr:
    # test_tarディレクトリを作成しファイルを展開
    # tr.extractall(path='test_tar')

    # 展開せずにファイルの中身を見る
    with tr.extractfile('./file/test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())
import os
import pathlib
import glob
import shutil

# print(os.path.exists('./file/test.txt'))
# print(os.path.isfile('./file/test.txt'))
# print(os.path.isdir('file'))

# os.rename('./file/test.txt', './file/renamed.txt')
# os.symlink('file/renamed.txt', '/app/file/symlink.txt')
# with open('./file/symlink.txt', 'r') as f:
#     print(f.read())

# ディレクトリを作成
# os.mkdir('./file/test_dir')
# ディレクトリを削除（空の場合）
# os.rmdir('./file/test_dir')

# 空のファイルを作成
# pathlib.Path('./file/empty.txt').touch()
# ファイルを削除
# os.remove('./file/empty.txt')

# os.mkdir('./file/test_dir')
# os.mkdir('./file/test_dir/test_dir2')
# ディレクトリ名をリスト表示 -> ['test_dir2']
# print(os.listdir('./file/test_dir'))

# pathlib.Path('./file/test_dir/test_dir2/empty.txt').touch()
# ファイル名をリスト表示 -> ['./file/test_dir/test_dir2/empty.txt']
# print(glob.glob('./file/test_dir/test_dir2/*'))

# ファイルをコピー
# shutil.copy('./file/test_dir/test_dir2/empty.txt', 
#             './file/test_dir/test_dir2/empty2.txt')
# print(glob.glob('./file/test_dir/test_dir2/*'))

# ディレクトリを中身ごと削除（要注意）
# shutil.rmtree('./file/test_dir')

# 現在のディレクトリを取得
# print(os.getcwd())
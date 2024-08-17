# コマンド引数
# import sys
# print(sys.argv)

# python argument.py a b c

# -> ['argument.py', 'a', 'b', 'c']

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--head')
parser.add_argument('body', nargs='+')
args = parser.parse_args()
print(args)

# python basic/argument.py --head=1 2 3
# Namespace(head='1', body=['2', '3'])

# nargs
"""
引数の数を指定できる。
nargs=2だと、引数を丁度2個受け取る。（過不足は許されない）
nargs='*'の場合、引数はいくつでも良い（defaultが設定されていれば0でも）
nargs='+'の場合は1以上の引数（defaultが使えない）
"""

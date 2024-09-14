import contextlib
import logging
# import sys


# 標準入力
# x = input('Enter:')
# for line in sys.stdin:
#     print(line)

# 標準出力
# print('hello')
# sys.stdout.write('hello\n')

# 標準エラー
# logging.error('Error!')
# sys.stderr.write('Error!\n')

# 標準出力の結果をlogファイルに出力
with open('library/_contextlib/stdout.log', 'w') as f:
    with contextlib.redirect_stdout(f):
        print('hello')
        
with open('library/_contextlib/stderr.log', 'w') as f:
    with contextlib.redirect_stderr(f):
        logging.error('Error!')

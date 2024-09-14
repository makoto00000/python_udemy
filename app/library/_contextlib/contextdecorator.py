# classの形式で、実行したい処理の前後の処理を記述することができる。

import contextlib


class tag(contextlib.ContextDecorator):
    def __init__(self, name):
        self.name = name
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)

    def __enter__(self):
        print(self.start_tag)

    def __exit__(self, exc_type, exc_val, exc_tb):  # エラーハンドリングもできる
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print(self.end_tag)


with tag('h2'):
    # raise Exception('error')
    print('test')

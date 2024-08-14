# 標準モジュールをアルファベット順に
import os
import sys

# 1行あけてサードパーティーのモジュール
import flask

# 1行あけて自分で作成したモジュールを読み込む

# インポートするときはモジュールを読み込む
# NG 関数を使用するときに、読み込んだものかファイル内で定義したものかわからない
from app.controller.module import function
function()

# OK 使用するときは冗長になるがインポートしてきたものだと一目で分かる
import app.controller.module
app.controller.module.function()

class MainError(Exception):
    pass

def main():
    raise MainError

# 以下のような内包表記は避ける
x = [(i, x, y) for i in [1, 2, 3] for x in [1, 2, 3] for y in [1, 2, 3]]

for i in [1, 2, 3]:
    for x in [1, 2, 3]:
        for y in [1, 2, 3]:
            print(i, x, y)

d = {'key1': 'value1', 'key2': 'value2'}

# 辞書は最初からkeyをみてくれるので、keysメソッドを使う必要がない
if 'key1' in d:
    print('test')

if 'key1' in d.keys():
    print('test')

# 変数名はk, vのようにするのではなく分かりやすく
ranking = {'a': '1', 'b': '2'}
for name, count in ranking.items():
    print(name, count)


# ジェネレーターを使っても良いときはその方が高速
# def t():
#     num = []
#     for i in range(10):
#         num.append(i)
#     return num

# t()を実行するたびに1回ずつforループが回り値を返す
def t():
    for i in range(10):
        yield i


for i in t():
    print(i)


# ラムダ関数 下２つは同じ
# 単純な関数を定義する場合はlambdaを使う方がスッキリ
def test_func(x):
    return x * 2

lambda x: x * 2

# 後置if 1行で書ける
y = None
x = 1 if y else 2
print(x)  # x = 2


# list=[]と書くとクラス間で共通のリストになってしまうので中で初期化する
class Test(object):
    def arr_func(self, list=None):
        if list is None:
            list = []


# baseに10を先に入れておいて、後からplusを実行する
def base(x):
    def plus(y):
        return x + y
    return plus


# グローバル変数を使わずに以下のように書く
plus = base(10)
print(plus(10))  # 20
print(plus(30))  # 40


# デコレーター
class Test2(object):

    def _decorator(func):
        def wrapper(self):
            print('pre')
            return func(self)
        return wrapper
    
    @_decorator
    def method():
        print('main method')
    
    # 以下のようにも書けるが古い書き方
    # method = _decorator(method)


test = Test2()
test.method()
# pre
# main method

if __name__ == '__main__':
    main()

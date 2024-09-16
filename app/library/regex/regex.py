import re


m = re.match('a.c', 'abc')  # 文字列の先頭で判定
print(m.span())  # 0~3文字目
print(m.group())


m = re.search('a.c', 'test abc test')
print(m.span())  # 5~8文字目まで
print(m.group())


m = re.findall('a.c', 'test abc test abc')  # 配列を返す
print(m)  # ['abc', 'abc']


m = re.finditer('a.c', 'test abc test abc')  # イテレーターを返す
print([w.group() for w in m])  # ['abc', 'abc']


m = re.match('ab?', 'ab')  # aとbが0個か1個
m = re.match('ab*', 'ab')  # aとbが0個以上
m = re.match('ab+', 'a')  # aとbが1個以上
m = re.match('a{3}', 'aaa')  # aが3個
m = re.match('a{2,4}', 'aaa')  # aが2から4個
m = re.match('[a-zA-Z0-9]', 'b')  # 英数字とアンダースコア
m = re.match('\w', 'A')  # 英数字とアンダースコア
m = re.match('[^a-zA-Z0-9]', 'b')  # 英数字とアンダースコア以外
m = re.match(r'\W', 'a')  # 英数字アンダースコア以外
m = re.match(r'\d', '1')  # 0-9の数字
m = re.match(r'\D', '1')  # 0-9の数字以外
m = re.match('a|b', 'x')  # aかb
m = re.match('(abc)+', 'abc')  # abcのかたまりが1個以上
m = re.match(r'\s', ' ')  # スペース
m = re.match(r'\S', ' ')  # スペース以外
m = re.match(r'\*', '*')  # 特殊文字はバックスラッシュをつける
m = re.search('^abc', 'abc test')  # 先頭がabc
m = re.match('abc$', 'test abc')  # 最後がabc
m = re.match('', '')
m = re.match('', '')
print(m)

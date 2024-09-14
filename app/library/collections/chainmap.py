import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}

# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)

# {'a': 'a', 'c': 'c', 'num': 0}
# 存在しなかったbが追加され、cが上書き
# {'a': 'a', 'c': 'cc', 'num': 0, 'b': 'b'}
# bとcが上書き
# {'a': 'a', 'c': 'ccc', 'num': 0, 'b': 'bbb'}

# 複数の辞書を管理。参照しているだけなので、もとの辞書が変更されても反映される。

m = collections.ChainMap(a, b, c)
print(m)
print(m.maps)
print(m['c'])

# ChainMap({'a': 'a', 'c': 'c', 'num': 0}, {'b': 'b', 'c': 'cc'}, {'b': 'bbb', 'c': 'ccc'})
# [{'a': 'a', 'c': 'c', 'num': 0}, {'b': 'b', 'c': 'cc'}, {'b': 'bbb', 'c': 'ccc'}]
# c

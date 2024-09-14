import collections

# 配列の文字の数を辞書に保存する
d = {}
list = ['a', 'a', 'a', 'b', 'b', 'c']

for word in list:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(d)


# setdefaultを使う
d = {}
list = ['a', 'a', 'a', 'b', 'b', 'c']

for word in list:
    d.setdefault(word, 0)  # wordのkeyがなかったらデフォルトの値をいれる
    d[word] += 1
print(d)


# defaultdictを使う
#  int型の辞書であると明示する
d = collections.defaultdict(int)
list = ['a', 'a', 'a', 'b', 'b', 'c']

for word in list:
    d[word] += 1
print(d)

# 集合型を用いる
d = collections.defaultdict(set)
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 5)]
for k, v in s:
    d[k].add(v)
print(d)
# {'red': {1, 3}, 'blue': {2, 4, 5}})
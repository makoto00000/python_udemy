import collections

# 辞書の順番が重要なときは、OrderedDictを使用する

od1 = collections.OrderedDict(
    {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
)
od2 = collections.OrderedDict(
    {'apple': 4, 'banana': 3, 'pear': 1, 'orange': 2}
)

d1 = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
d2 = {'apple': 4, 'banana': 3, 'pear': 1, 'orange': 2}

# 通常の辞書は順番が変わっても同じものと判定される
print(od1)
print(od1 == d1)  # True
print(od1 == d2)  # True

# OrderedDictは順番が違えば違い辞書と判定される
print(od1 == od2)  # False

d = {'apple': 4, 'banana': 3, 'pear': 1, 'orange': 2}
# keyの昇順で並び替え
od = collections.OrderedDict(
        sorted(d.items(), key=lambda t: t[0]))
# sorted(d.items(), key=lambda t: t[1])) # valueの昇順
print(od)

od = collections.OrderedDict(d)
print(od)
od['cc'] = 100  # 最後に追加される
print(od)

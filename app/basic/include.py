# リスト内包表記

t = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)

r = [i for i in t]
r2 = [i for i in t if i % 2 == 0]
r3 = [i + j for i in t for j in t2] # 二重ループ
print(r)
print(r2)
print(r3)
# [1, 2, 3, 4, 5]
# [2, 4]
# [7, 8, 9, 10, 11, 8, 9, 10, 11, 12, 9, 10, 11, 12, 13, 10, 11, 12, 13, 14, 11, 12, 13, 14, 15]

# 辞書内包表記

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {x: y for x, y in zip(w,f)}
print(d)
# {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'

# 集合内包表記

s = {i for i in range(10)}
print(s)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# ジェネレーター内包表記

g = (i for i in range(10)) # ※
for x in g:
  print(x)

# ※ 以下と同じ
# def g():
#   for i in range(10):
#     yield i
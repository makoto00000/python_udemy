# ジェネレーター

def greeting():
  yield 'Good Morning'
  yield 'Good Afternoon'
  yield 'Good night'

def counter():
    for i in range(10):
      yield i

g = greeting()
c = counter()

# print(next(c))
# print(next(g))

# print(next(c))
# print(next(g))

# print(next(c))
# print(next(g))

for i in c:
    print(i)


#nextを実行するたびにyieldを実行する。好きなタイミングで呼び出すことができる。

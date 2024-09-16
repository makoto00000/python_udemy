import datetime


# repr representation
# pythonオブジェクトの形式を出力

print('s')
print(str('s'))
print(repr('s'))
# s
# s
# 's'

d = datetime.datetime.now()
print(d)
print(str(d))
print(repr(d))
# 2024-09-14 23:54:06.500425
# 2024-09-14 23:54:06.500425
# datetime.datetime(2024, 9, 14, 23, 54, 6, 500425)


# formatを使ってreprを表示 !r

print('{!r} {} {!s}'.format('test', 'test1', 'test2'))
# 'test' test1 test2


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):  # reprをオーバーライド
        return 'Point<object>'

    def __str__(self):  # strをオーバーライド
        return 'Point ({}, {})'.format(self.x, self.y)


p = Point(10, 200)
print('{0!r}'.format(p))
print('{0} '.format(p))
print('{0!s}'.format(p))
# Point<object>
# Point (10, 200)
# Point (10, 200)

# adminとして、クラスの中身をformatで表示するみたいな使い方ができる。

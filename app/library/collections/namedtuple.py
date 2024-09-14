import collections

p = (10, 20)
print(p[0])


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(10, 20)
print(p.x)  
p.x = 50  # 書き換えができてしまう
print(p.x)  # 50


Point = collections.namedtuple('Point', ['x', 'y'])
# Point = collections.namedtuple('Point', ['x, y')  文字列でもよい
p = Point(10, y=20)
print(p.x)
# p.x = 50  # AttributeError: can't set attribute
print(p)


p1 = Point._make([100, 200])  # 新しいタプルを作成
print(p1)
print(p1._asdict())  # 辞書型に変換

p1._replace(x=500)
print(p1)
p2 = p1._replace(x=500)  # p1の値を一部変更してp2を作る
print(p2)


class SumPoint(collections.namedtuple('Point', 'x, y')):
    @property  # propertyを設定することができる
    def total(self):
        return self.x + self.y


p3 = SumPoint(2, 3)
print(p3.x, p3.y, p3.total)

# クラス変数

class Person(object):

    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind) # クラス変数のkindを参照する

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

class T(object):

# 以下の書き方だとクラス変数が共有されてしまう
#   words = []

# 以下の書き方ならインスタンス化のときに初期化される
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)

d = T()
d.add_word('add 3')
d.add_word('add 4')
print(d.words)

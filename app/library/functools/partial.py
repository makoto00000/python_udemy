import functools


def f(x, y):
    return x + y


def task(f):
    print('start')
    print(f(10, 20))


task(f)
task(lambda x, y: x + y)


# outerを定義することで、task内で引数を渡さなくてよくなる
def outer(x, y):
    def inner():
        return x + y
    return inner


def task(f):
    print('start')
    print(f())


f = outer(10, 20)
task(f)


# functoolsで簡単に

def f(x, y):
    return x + y


p = functools.partial(f, 10, 20)
task(p)

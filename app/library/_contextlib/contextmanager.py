import contextlib


# contextmanagerを使わない場合

def tag(name):
    def _tag(f):
        def _wrapper(content):
            print('<{}>'.format(name))
            r = f(content)
            print('</{}>'.format(name))
            return r
        return _wrapper
    return _tag


@tag('h2')
def f(content):
    print(content)


f('test')


# contextmanagerを使う場合


@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield
    print('</{}>'.format(name))


# decorator

@tag('h2')
def f(content):
    print(content)


f('test')


# with

with tag('h2'):
    print('test')

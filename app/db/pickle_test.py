import pickle


class T(object):
    def __init__(self, name):
        self.name = name


data = {
  'a': [1, 2, 3],
  'b': ('test', 'test'),
  'c': {'key': 'value'},
  'd': T('test')
}

with open('db/data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('db/data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(data_loaded)
    print(data_loaded['d'].name)
    print(type(data_loaded['a']))
    print(type(data_loaded['b']))
    print(type(data_loaded['c']))
    print(type(data_loaded['d']))

# 以下のようにpythonのデータのまま取り出すことができる
# {'a': [1, 2, 3], 'b': ('test', 'test'), 'c': {'key': 'value'}, 'd': <__main__.T object at 0xffff958e3f70>}
# test
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>
# <class '__main__.T'>

# pythonでしか使えないので、他の言語に移行はできない。

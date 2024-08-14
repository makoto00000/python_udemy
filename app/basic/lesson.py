# *args 配列を展開してタプルに
# **kwargs  辞書を展開
def menu(word, *args, **kwargs):
    """
    これはドキュメントです
    """
    print(word)
    print(type(args))
    print(type(kwargs))

w = 'banana'
a = ['apple', 'grape']
d = {'x': 100, 'y': 200}
menu(w, *a, **d)
print(menu.__doc__)
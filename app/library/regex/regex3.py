import re

# 分割
s = 'My name is ... Mike'

print(s.split())  # ['My', 'name', 'is', '...',  'Mike']

# re.compileの方が柔軟に指定できる
p = re.compile(r'\W+')
print(p.split(s))  # ['My', 'name', 'is', 'Mike']


# 置換
p = re.compile('(blue|white|red)')
print(p.sub('color', 'blue socks and red shoes'))
print(p.sub('color', 'blue socks and red shoes', count=1))
print(p.subn('color', 'blue socks and red shoes'))
# color socks and color shoes
# color socks and red shoes
# ('color socks and color shoes', 2) タプル形式


def hexrepl(match):
    value = int(match.group())
    return hex(value)


p = re.compile(r'\d')
print(p.sub(hexrepl, '12345 55 11 test test2'))
# 0x10x20x30x40x5 0x50x5 0x10x1 test test0x2

# sub関数が正規表現に一致した文字をhexreplに引数として渡してくれる。
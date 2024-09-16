
print(('{}, {}, {}'.format('a', 'b', 'c')))  # a, b, c
print(('{0}, {1}, {2}'.format('a', 'b', 'c')))  # a, b, c
print(('{2}, {1}, {0}'.format('a', 'b', 'c')))  # c, b, a

print('{name} {family}, {family} {name}'.format(name='jun', family='sakai'))
# jun sakai, sakai jun

t = (1, 2, 3)
print('{0[0]} {0[2]}'.format(t))  # 1 3
print('{t[0]} {t[2]}'.format(t=t))  # 1 3

print('{} {}'.format(*t))  # 1 2
print('{0} {2}'.format(*t))  # 1 3
print('{0} {1} {2}'.format(1, 2, 3))  # 1 3

d = {'name': 'jun', 'family': 'sakai'}
print('{0[name]} {0[family]}'.format(d))
print('{name} {family}'.format(**d))
# print('{name} {family}, {family} {name}'.format(name='jun', family='sakai'))
# と同じ


print('{:<30}'.format('left'))
print('{:>30}'.format('right'))
print('{:^30}'.format('center'))
# left                          
#                          right
#             center            

print('{:*^30}'.format('center'))
# ************center************

print('{name:*^30}'.format(name='center'))
# ************center************

print('{name:{fill}{align}{width}}'.format(
      name='center', fill='*', align='^', width=30))
# ************center************

print('{:,}'.format(123456789))
# 123,456,789

print('{:+f} {:+f}'.format(3.14, -3.14))
print('{:f} {:f}'.format(3.14, -3.14))
print('{:-f} {:-f}'.format(3.14, -3.14))
# +3.140000 -3.140000
# 3.140000 -3.140000
# 3.140000 -3.140000

# 有効桁数
print('{}'.format(19/22))
print('{:.2%}'.format(19/22))
# 0.8636363636363636
# 86.36%


# 100 0x64 0o144 0b1100100
# 10進数 16進数 8進数 2進数
print(int(100), hex(100), oct(100), bin(100))
print('{0:d} {0:#x} {0:#o} {0:#b}'.format(100))
print('{0:d} {0:x} {0:o} {0:b}'.format(100))
# 100 0x64 0o144 0b1100100
# 100 0x64 0o144 0b1100100
# 100 64 144 1100100

# bdX 2進数 10進数 16進数（アルファベット大文字表記）で1~20を5桁表示で出力
for i in range(20):
    for base in 'bdX':
        print('{:5{base}}'.format(i, base=base), end=' ')
    print()

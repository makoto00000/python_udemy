import collections
import queue

collections.deque

q = queue.Queue()  # FIFO
lq = queue.LifoQueue()  # LIFO(スタック)
list = []
d = collections.deque()  # 高速に動作する


for i in range(3):
    q.put(i)
    lq.put(i)
    list.append(i)
    d.append(i)

# print(d[1])  # indexでも参照できる
# # ローテーションできる [0, 1, 2]
# d.rotate()  # deque([2, 0, 1])
# d.rotate()  # deque([1, 2, 0])

# d.extendleft('x')  # 先頭に追加
# d.extend('y')  # 末尾に追加

for _ in range(3):
    print('FIFO queue = {}'.format(q.get()))
for _ in range(3):
    print('LIFO queue = {}'.format(lq.get()))
for _ in range(3):
    print('list       = {}'.format(list.pop()))
    # print('list       = {}'.format(list.pop(0)))
for _ in range(3):
    print('deque      = {}'.format(d.pop()))  # スタックとして
    # print('deque      = {}'.format(d.popleft()))  # キューとして

# FIFO queue = 0
# FIFO queue = 1
# FIFO queue = 2
# LIFO queue = 2
# LIFO queue = 1
# LIFO queue = 0
# list       = 2
# list       = 1
# list       = 0
# deque      = 2
# deque      = 1
# deque      = 0

d. clear()  # 中身を消去
print(d)
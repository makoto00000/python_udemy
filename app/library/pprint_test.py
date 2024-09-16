import json
import pprint

list = ['apple', 'orange', 'banana', 'peach', 'mango']
list.insert(0, list[:])
list.insert(0, list[:])
list.insert(0, list[:])
list.insert(0, list[:])

# print(list)

# printを拡張して出力形式を自由に設定できる
pp = pprint.PrettyPrinter(
    indent=4, width=40, compact=True, depth=3)
pp.pprint(list)


d = {'a': 'A', 'b': 'B', 'c': {'x': {'y': 'Y'}}}
pp = pprint.PrettyPrinter(
    indent=4, width=40
)

pp.pprint(d)

# {   'a': 'A',
#     'b': 'B',
#     'c': {'x': {'y': 'Y'}}}


# json形式の場合
# pprintほどオプションは多くない
# タプルはリストになるのでpprintの方が良い
print(json.dumps(d, indent=4))

# {
#     "a": "A",
#     "b": "B",
#     "c": {
#         "x": {
#             "y": "Y"
#         }
#     }
# }

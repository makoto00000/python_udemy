import collections
# d = collections.defaultdict(int)
d = {}
s = 'myg'

for key in s:
    if not key in d:
        d[key] = 0
    d[key] += 1

print(d.get('a'))
print(d['a']) #KeyError defaultdictなら0をいれてくれるのでエラーにならない（0を返す）
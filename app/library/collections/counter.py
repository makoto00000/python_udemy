import collections

list = ['a', 'a', 'a', 'b', 'b', 'c']
c = collections.Counter()
for word in list:
    c[word] += 1

print(c)
print(c.most_common(2))
print(sum(c.values()))

# ファイルを読み込んで、含まれる単語の使用頻度が高い順に20個出力
import re
with open('library/collections/counter.py', 'r') as f:
    words = re.findall(r'\w+', f.read().lower())
    print(collections.Counter(words).most_common(20))

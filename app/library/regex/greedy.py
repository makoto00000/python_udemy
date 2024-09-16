import re

s = '<html><head><title>Title</title></head></html>'

# 最長の一致を探す（最初の<から最後の>までがマッチする
print(re.match('<.*>', s))

# 最短の一致を探す（最初の<から
print(re.match('<.*?>', s))

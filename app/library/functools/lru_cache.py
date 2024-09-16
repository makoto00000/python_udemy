import functools


@functools.lru_cache(maxsize=5)  # 最大5個まで値を保持
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r


for i in range(10):
    print(long_func(i))

print(long_func.cache_info())
# CacheInfo(hits=0, misses=10, maxsize=128, currsize=10)

print('next run')

# 1回目の後半5個しか保存されていないので、2回目の前半5個は再度関数を実行する。
# 2回目の前半5回でキャッシュは上書きされるので、結局10回全て関数を実行する。

for i in range(10):
    print(long_func(i))

print(long_func.cache_info())

long_func.cache_clear()

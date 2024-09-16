# 関数の結果を辞書に保存しておき、次同じ値が呼ばれたら関数を実行せずにメモから値を返す

def memoize(f):
    memo = {}

    def _wrapper(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return _wrapper


@memoize
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r


for i in range(10):
    print(long_func(i))

for i in range(10):
    print(long_func(i))

# 関数内関数

def mainfunction(a, b):

    def subfunction(c, d):
        return c + d

    print(subfunction(a, b))


mainfunction(2, 4)

# subfunctionは外に出して書くこともできるが、mainfunctionの中でしか使わない関数なので、まとめるほうが分かりやすい。
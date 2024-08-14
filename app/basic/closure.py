# クロージャー

def circle_area_func(pi):
    def circle_area(radius):
        return radius * radius * pi

    return circle_area # circle_areaを返す

# circle_area_funcにpiだけ入れておいて、circle_areaを変数に入れておく
ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

# circle_areaを実行したいタイミングで、circle_areaの引数とともに呼びだす。
print(ca1(10)) 
print(ca2(10))

# 外側の関数で値を保持しておいて、すぐに実行せず、好きなときに内側の関数を実行できる。
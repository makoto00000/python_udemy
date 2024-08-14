# スタイルルール

# セミコロン不要
# x = 1;
# y = 2;

# 1行の文字数は80文字以内
x = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


# 改行は2行
# 引数が長くなる場合は改行して先頭を揃える
def test_func(x, y, z,
              dsfasfhdjaksfhdjkalfhjdkahfjakshfjaklh='test'):
    # インデントは半角空白4つ
    """_summary_
    # 変更することがあれば名前も入れる
    # TODO (name) ~~~~~~
    Args:
      x (_type_): _description_
      y (_type_): _description_
      z (_type_): _description_
      dsfasfhdjaksfhdjkalfhjdkahfjakshfjaklh (str, optional):
      _description_. Defaults to 'test'.
      # URLは80文字超えてもOK
      https://hfdjksafhdsajfdklsajfdklsa;fjkla;jfadfjskflafdsafdsafsada.com/document
    """
    print('test')


# if (x and y)のような場合はかっこ不要
# if (x and y) or (a and b) のように書くならOK
if x:
    print('exist')

    # 複数行で書く場合
    x = {
        'test': 'sss'
    }

    # 1行で書く場合
    x = {'test': 'sss'}

    # =の前後は半角スペース
    x = 1
    y = 2

    # カンマの前はスペースなし、後ろに一つ
    x, y = y, x

    # =は縦に揃えなくて良い
    x = 100
    yyyyy = 200
    zzzzzzzzz = 300


# 文字列の連結は単純なものなら+演算子で
# 複雑なものならformat
word = 'hello'
word2 = "!"
new_word = '{}{}'.format(word, word2)  # NG
new_word = word + word2  # OK
new_word = '{} ######### {}'.format(word, word2)  # OK
new_word = word + '#########' + word2  # NG


# ループ内で文字列の連結

long_word = ""
long_word_arr = []
for word in ['afdsaf', 'hjkgfds', 'rtewioar']:
    # メモリ効率は悪い
    # long_word += word

    # appendで配列に入れてから結合する
    long_word_arr.append(word)
new_long_word = ''.join(long_word_arr)
print(new_long_word)


# シングルクォートとダブルクォート
print('Hello')  # 単純な文字列ならシングル
name = 'Mike'
print("Hello {}!".format(name))  # 展開させるならダブル


# if文は2行でも1行でも書けるがルールに従う
if x:
    print('exit')

if x: print('exit')


# クラス名はキャメルケース、関数名、変数名、プロパティはスネークケース
# グローバル変数は全部大文字

DEFAULT_NAME = 'Steve'


class Test(object):
    def __init__(self, user_name=""):
        self.__user_name = user_name

    @property
    def user_name(self):
        return self.__user_name

    def run(self):
        print('run')


test = Test('Mike')
print(test.user_name)
test.run()


# main.pyには明示的に書く

def main():
    test = Test()
    test.run()


if __name__ == '__main__':
    main()

# このファイルが他から呼び出されてしまった場合にも実行されてしまうので、mainのときだけ実行されるようにする。

# ラムダ

l = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat' ,'sun']
def change_words(words, func):
  for word in words:
    print(func(word)) #wordを渡すだけ

# def sample_func(word):
#   return word.capitalize()

# change_words(l, sample_func)

# 引数wordを受け取ってcapitalizeを実行している
change_words(l, lambda word: word.capitalize())

# わざわざ関数を定義するほどでもないときに1行でサッと書ける。
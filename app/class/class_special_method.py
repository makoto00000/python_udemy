# 特殊メソッド

class Word(object):
    def __init__(self, text):
        self.text = text
    
    def __str__(self): # strやprintを使ったときに呼び出される
        return 'Word!!!!!!'
    
    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()
    
    def __eq__(self, word):
        return self.text.lower() == word.text.lower()
    
w = Word('test')
w2 = Word('#####')
w3 = Word('test')
print(w) # Word!!!!!!
print(len(w)) # 4
print(w + w2) # test#####
print(w == w3) # True

# 例外処理

l = [1,2,3]
i = 5

try:
  l[0]
except IndexError as ex:
  print("Dont worry: {}" .format(ex))
except NameError as ex:
  print("Dont worry: {}" .format(ex))
except Exception as ex:
  print("Other: {}" .format(ex))
else: # tryに成功したときのみ実行
  print('done')
finally: # 成功失敗に関係なく必ず実行
  print('clean up')

# 独自例外の作成

class UppercaseError(Exception): # Exceptionを継承してエラークラスを作成
  pass

def check():
  words = ['APPLE', 'orange', 'banana']
  for word in words:
    if word.isupper():
      raise UppercaseError(word)

try:
  check()
except UppercaseError as exc:
  print('This is my fault. Go next')
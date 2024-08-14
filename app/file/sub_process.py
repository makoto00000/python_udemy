import subprocess

# ターミナルで ls -alを実行する
subprocess.run(['ls', '-al'])

# 以下の方法であればパイプも使えるがシェルインジェクションの標的になってしまう。
# subprocess.run('ls -al | grep test', shell=True)

# 以下のようにしてパイプラインを繋ぐ
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
output = p2.communicate()[0]
print(output)
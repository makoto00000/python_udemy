import string
import random

# pip install pycryptodome
from Crypto.Cipher import AES


print(AES.block_size)  # 16
print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

# ascii_lettersから16個の文字をランダムに取得する
key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)).encode(
        'utf-8')
print(key)

# 初期ベクトル
iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)).encode(
        'utf-8')
print(iv)

plaintext = 'abcdefghijklmnopqrstuvwxyz'
cipher = AES.new(key, AES.MODE_CBC, iv)

# plaintextはblock_sizeの倍数である必要があるので文字数を調整
padding_length = AES.block_size - len(plaintext) % AES.block_size
plaintext += chr(padding_length) * padding_length

cipher_text = cipher.encrypt(plaintext.encode('utf-8'))
print(cipher_text)

# 復号化
cipher2 = AES.new(key, AES.MODE_CBC, iv)
decrypted_text = cipher2.decrypt(cipher_text)
print(decrypted_text)
print(decrypted_text[-1])
print(decrypted_text[:-decrypted_text[-1]])

# ファイルを読み取って暗号化しえｔdat出力
with open('crypto/plaintext', 'r') as f, open('crypto/enc.dat', 'wb') as e:
    plaintext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length
    cipher_text = cipher.encrypt(plaintext.encode('utf-8'))
    e.write(cipher_text)

# datファイルを復号化
with open('crypto/enc.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher2.decrypt(cipher_text)
    print(decrypted_text[:-decrypted_text[-1]].decode('utf-8'))

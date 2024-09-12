import base64
import os
import hashlib

user_name = 'user1'
user_pass = 'password'
db = {}

salt = base64.b64encode(os.urandom(32))
print('salt', salt)


def get_digest(password):
    password = bytes(password, 'utf-8')
    digest = hashlib.sha256(salt + password).hexdigest()  # saltを付け加える
    for _ in range(10000):  # digestを10000回作成する
        digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
    return digest


# 上記のhash化を実現した関数が用意されている。
# digest = hashlib.pbkdf2_hmac(
#     'sha256', bytes(user_pass, 'utf-8'), salt, 10000)


db[user_name] = get_digest(user_pass)


def is_login(user_name, password):
    return get_digest(password) == db[user_name]


print(is_login(user_name, 'password'))  # True
print(is_login(user_name, 'test'))  # False

# 1回hash化するだけでは、もとの値を推測できる可能性がある。
# saltを足したり、hash化を何回も繰り返して、推測されにくくする。

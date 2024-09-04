import requests

# r = requests.post(
#     'http://127.0.0.1:5000/post', data={'username': 'mike'}
# )
# print(r.text)

r = requests.get('http://127.0.0.1:5000/employee/mike')
print(r.text)

r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'mike'})
print(r.text)

r = requests.get('http://127.0.0.1:5000/employee/mike')
print(r.text)

r = requests.put('http://127.0.0.1:5000/employee', data={
    'name': 'mike', 'new_name': 'john'})
print(r.text)

r = requests.get('http://127.0.0.1:5000/employee/john')
print(r.text)

r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'john'})
print(r.text)

r = requests.get('http://127.0.0.1:5000/employee/john')
print(r.text)

# 出力結果
# No
# created mike
# 1:mike
# updated mike: john
# No

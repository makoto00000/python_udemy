import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}

url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# http://httpbin.org/get?key1=value1&key2=value2

with urllib.request.urlopen(url) as f:
    print(json.loads((f.read().decode('utf-8'))))

# {'args': {'key1': 'value1', 'key2': 'value2'}, 'headers': {'Accept-Encoding': 'identity', 'Host': 'httpbin.org', 'User-Agent': 'Python-urllib/3.9', 'X-Amzn-Trace-Id': 'Root=1-66d7a137-740991a504bf8b27295de371'}, 'origin': '219.106.160.211', 'url': 'http://httpbin.org/get?key1=value1&key2=value2'}

print('##################')

payload = json.dumps(payload).encode('utf-8')  # json → str → bytes
req = urllib.request.Request(
    'http://httpbin.org/post', data=payload, method='POST')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

# {'args': {}, 'data': '', 'files': {}, 'form': {'{"key1": "value1", "key2": "value2"}': ''}, 'headers': {'Accept-Encoding': 'identity', 'Content-Length': '36', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'Python-urllib/3.9', 'X-Amzn-Trace-Id': 'Root=1-66d7a245-3755223267f5bea238275318'}, 'json': None, 'origin': '219.106.160.211', 'url': 'http://httpbin.org/post'}

print('##################')

payload = json.dumps(payload).encode('utf-8')  # json → str → bytes
req = urllib.request.Request(
    'http://httpbin.org/put', data=payload, method='PUT')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

print('##################')

payload = json.dumps(payload).encode('utf-8')  # json → str → bytes
req = urllib.request.Request(
    'http://httpbin.org/delete', data=payload, method='DELETE')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

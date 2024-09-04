import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"},
        ]
}

print('############')
a = json.dumps(j)  # dumps: 辞書型 → 文字列
print(json.loads(a))  # loads: 文字列 → 辞書型

print('############')
with open('web/test.json', 'w') as f:
    json.dump(j, f, indent=4)  # dump: 辞書型 → jsonファイル

with open('web/test.json', 'r') as f:
    print(json.load(f))  # load: jsonファイル → 辞書型

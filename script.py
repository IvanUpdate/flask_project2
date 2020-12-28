import json


with open('data.py', 'r', encoding='utf-8') as r:
    records = r.read()
with open('data.json', 'w', encoding='utf-8') as w:
        json.dump(records, w)



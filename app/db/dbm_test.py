import dbm

with dbm.open('db/cache.db', 'c') as db:
    db['key1'] = 'value1'  # byte or string only
    db['key2'] = 'value2'

with dbm.open('db/cache.db', 'r') as db:
    print(db.get('key1'))

# b'value1'

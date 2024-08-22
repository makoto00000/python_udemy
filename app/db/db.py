import sqlite3

conn = sqlite3.connect('db/test_sqlite.db')

# インメモリーで実行する（DBには反映されない）
# conn = sqlite3.connect(':memory:')

curs = conn.cursor()

# CREATE
# curs.execute(
#     'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
# )
# conn.commit()

# curs.execute(
#     'INSERT INTO persons(name) values("Mike")'
# )

# curs.execute(
#     'SELECT * FROM persons'
# )
# print(curs.fetchall())

# curs.execute(
#     'INSERT INTO persons(name) values("Nancy")'
# )
# curs.execute(
#     'INSERT INTO persons(name) values("Jun")'
# )

# conn.commit()

# UPDATE
# curs.execute(
#     'UPDATE persons set name = "Michel" WHERE name = "Mike"'
# )
# conn.commit()

# DELETE
# curs.execute('DELETE FROM persons WHERE name = "Michel"')
# conn.commit()

# GET
curs.execute(
    'SELECT * FROM persons'
)
print(curs.fetchall())

curs.close()
conn.close()

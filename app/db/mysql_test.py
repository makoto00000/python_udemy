import mariadb

conn = mariadb.connect(
    user='root',
    password='root',
    database='test_mysql_database'
)

cursor = conn.cursor()
# cursor.execute(
#     'CREATE DATABASE test_mysql_database'
# )

# cursor.execute(
#     'CREATE TABLE persons('
#     'id int NOT NULL AUTO_INCREMENT,'
#     'name varchar(14) NOT NULL,'
#     'PRIMARY KEY(id))'
# )

# -> show create table persons;

# | persons | CREATE TABLE `persons` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `name` varchar(14) NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci |

# cursor.execute('INSERT INTO persons(name) values("Mike")')
# conn.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

cursor.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
# cursor.execute('DELETE FROM persons WHERE name = "Mike"')

cursor.close()
conn.close()

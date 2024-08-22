# SQLAlchemy データベースを変更してもコードの変更が不要
# pip install sqlalchemy

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# engine = sqlalchemy.create_engine('sqlite:///:memory:')
# echo=Trueとすると裏側の処理を表示できる
# engine = sqlalchemy.create_engine('sqlite:///db/test_sqlite2.db')

# rootだと失敗する
engine = sqlalchemy.create_engine(
    'mysql+pymysql://test_user:password@localhost/test_mysql_database2'
)

Base = sqlalchemy.orm.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)
session.commit()

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()

p4 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p4)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)

# sqlite3 db/test_sqlite2.db

# ユーザーを作成
# CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

# アクセス権限を付与
# GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';

# 権限をリロード
# FLUSH PRIVILEDGES;

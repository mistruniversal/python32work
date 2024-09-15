import psycopg2
"""
.cursor()
Метод курсор объект и конекшион возращает курсор - объект курсор через который можно отправлять запросы в базе данных,
 Для этого класс cursor представляет ряд методов
 1) execute(query,vars=None)


.comit-подтверждение транзакции
.fetchall-выводит все записи 
.fetchmany(3) - таже функция LIMIT в sql
.executemany - ограниченный список добавлений
"""

conn = psycopg2.connect(dbname='postgresL', user='postgres',password='user',host='127.0.0.1',port='5432')
cursor=conn.cursor()

# conn.autocommit = True
sql=f'CREATE DATABASE testdb1'

cursor.execute(sql)
print('БД успешно создана')


print(f'Есть подключение')
conn.close()
cursor.close()






conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
cursor=conn.cursor()

cursor.execute(
                'CREATE TABLE people('
               'id SERIAL PRIMARY KEY,'
               'name VARCHAR(50),'
               'age INTEGER)'
)
conn.commit()

conn.close()
cursor.close()






conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
cursor=conn.cursor()

cursor.execute(f"INSERT INTO people(name,age) VALUES('Tom',38")
conn.commit()



conn.close()
cursor.close()









conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
cursor=conn.cursor()


bob=('bob',12)
cursor.execute(f"INSERT INTO people(name,age) VALUES(%s,%s",bob)
conn.commit()


conn.close()
cursor.close()






people=[(1,2),(3,4),(5,6)]
conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
cursor=conn.cursor()

cursor.executemany(f"INSERT INTO people(name,age) VALUES(%s,%s)",people)
conn.commit()

conn.close()
cursor.close()









conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
cursor=conn.cursor()

cursor.execute("SELECT * FROM people")
print(cursor.fetchall())

conn.commit()

conn.close()
cursor.close()









conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
cursor=conn.cursor()

cursor.execute("SELECT * FROM people")
for person in cursor.fetchall():
    print(f"{person[1]}{person[2]}")

conn.commit()

conn.close()
cursor.close()






conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
cursor=conn.cursor()

cursor.execute("SELECT * FROM people")
print(cursor.fetchmany(3))

conn.commit()

conn.close()
cursor.close()




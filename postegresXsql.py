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
.fetchone() - выводит одну строчку
"""

# conn = psycopg2.connect(dbname='postgres', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# conn.autocommit = True
# sql='CREATE DATABASE testdb1'
#
# cursor.execute(sql)
# print('БД успешно создана')
#
#
# print(f'Есть подключение')
# conn.close()
# cursor.close()
#
#
#
#
#
#
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# cursor.execute(
#                 'CREATE TABLE people('
#                'id SERIAL PRIMARY KEY,'
#                'name VARCHAR(50),'
#                'age INTEGER)'
# )
# conn.commit()
#
# conn.close()
# cursor.close()

#
#
#
#
#
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# cursor.execute(f"INSERT INTO people(name,age) VALUES('Tom',38)")
# conn.commit()
#
#
#
# conn.close()
# cursor.close()
#
#
#
#
#
#
#
#
#
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
#
# bob=('bob',12)
# cursor.execute(f"INSERT INTO people(name,age) VALUES(%s,%s)",bob)
# conn.commit()
#
#
# conn.close()
# cursor.close()
#
#
#
#
#
#
# people=[(1,2),(3,4),(5,6)]
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# cursor.executemany(f"INSERT INTO people(name,age) VALUES(%s,%s)",people)
# conn.commit()
#
# conn.close()
# cursor.close()
#
#
#
#
#
#
#
#
#
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# cursor.execute("SELECT * FROM people")
# print(cursor.fetchall())
#
# conn.commit()
#
# conn.close()
# cursor.close()
#
#
#
#
#
#
#
#
#
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# cursor.execute("SELECT * FROM people")
# for person in cursor.fetchall():
#     print(f"{person[1]}{person[2]}")
#
# conn.commit()
#
# conn.close()
# cursor.close()
#
#
#
#
#
#
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# cursor.execute("SELECT * FROM people")
# print(cursor.fetchmany(3))
#
# conn.commit()
#
# conn.close()
# cursor.close()
#
#
#
#
#
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# cursor.execute("SELECT * FROM people")
# print(cursor.fetchone())
#
# conn.commit()
#
# conn.close()
# cursor.close()


# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# # cursor.execute("UPDATE people SET name = 'Tomas' WHERE name = 'Tom'")
# # cursor.execute("UPDATE people SET name = %s WHERE name = %s",('Tom','Tomas'))
# cursor.execute('SELECT * FROM people')
# print(cursor.fetchall())
# conn.commit()
# conn.close()
# cursor.close()














# people=[(15,'bob'),(40,'Tom')]
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# cursor.executemany("UPDATE people SET age = %s WHERE name = %s",people)
#
# conn.commit()
# conn.close()
# cursor.close()






# people=[('1',),('3',),('5',)]
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# cursor.executemany("DELETE FROM people WHERE name=%s",people)
#
# conn.commit()
# conn.close()
# cursor.close()








# func1=('Rafael','nou@gmail.com','+79999999')
# func2=('+7528815','Rafael')
# func3=('Igor','adspfvhu@gmail.com','+67176018',2)
# func4=('NULL',2)
# func5=(2,)
# func6=(1,'Rafael','nou@gmail.com','+79999999')
# conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
# cursor=conn.cursor()
#
# cursor.execute("CREATE TABLE Pfonetel"
#                "(id SERIAL PRIMARY KEY,"
#                "name VARCHAR(50),"
#                "email VARCHAR(20),"
#                "numphone VARCHAR(30) )")
#
#
#
# cursor.execute("INSERT INTO Pfonetel(name,email,numphone) VALUES (%s,%s,%s)",func1)
#
#
#
# cursor.execute("UPDATE Pfonetel SET numphone = %s WHERE name=%s",func2)
#
#
# cursor.execute("UPDATE Pfonetel SET name=%s,email = %s,numphone=%s WHERE id=%s",func3)
#
#
# cursor.execute("UPDATE Pfonetel SET numphone=%s WHERE id=%s",func4)
#
#
#
# cursor.execute("DELETE FROM Pfonetel WHERE id=%s",func5)
#
#
# cursor.execute("SELECT * FROM Pfonetel WHERE id=%s OR name=%s OR email=%s OR numphone=%s",func6)
# print(cursor.fetchall())
#
# conn.commit()
# conn.close()
# cursor.close()



# if __name__ == "__main__":
#     info = int(input(f'1.Создать таблицу'
#                     f'2.Добавить пользователя'
#                     f'3.Изменить значения пользователя'
#                     f'4.Изменить номер'
#                     f'5.Удалить пользователя'
#                     f'6.Вывести всю информацию'))
#     if info == 1:
#         a=input('Имя пользователя')
#         b=input('email пользователя')
#         f=input('телефон пользователя')
#         def funcone():
#             conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
#
#             cursor=conn.cursor()
#
#             cursor.execute("CREATE TABLE Pfonetel"
#                            "(id SERIAL PRIMARY KEY,"
#                            "name VARCHAR(50),"
#                            "email VARCHAR(20),"
#                            "numphone VARCHAR(30) )")
#             conn.commit()
#             conn.close()
#             cursor.close()
#         funcone()
#
#
#     elif info ==2:
#         a=input('Имя пользователя')
#         b=input('email пользователя')
#         f=input('телефон пользователя')
#         def funcone(a,b,f):
#             cortegh=(a,b,f)
#             conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
#
#             cursor=conn.cursor()
#
#             cursor.execute("INSERT INTO Pfonetel(name,email,numphone) VALUES (%s,%s,%s)",cortegh)
#
#
#             conn.commit()
#             conn.close()
#             cursor.close()
#         funcone(a,b,f)
#     elif info ==3:
#         id1=int(input('id пользователя'))
#         a=input('Имя пользователя')
#         b=input('email пользователя')
#         f=input('телефон пользователя')
#         def funcone(id,a,b,f):
#             cortegh=(a,b,f,id)
#             conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
#
#             cursor=conn.cursor()
#
#             cursor.execute("UPDATE Pfonetel SET name=%s,email = %s,numphone=%s WHERE id=%s",cortegh)
#
#             conn.commit()
#             conn.close()
#             cursor.close()
#         funcone(id1,a,b,f)
#     elif info ==4:
#         id1=int(input('id пользователя'))
#         f=input('телефон пользователя')
#         def funcone(id,f):
#             cortegh=(id,f)
#             conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
#
#             cursor=conn.cursor()
#
#             cursor.execute("UPDATE Pfonetel SET numphone=%s WHERE id=%s",cortegh)
#
#             conn.commit()
#             conn.close()
#             cursor.close()
#         funcone(id1,f)
#     elif info ==5:
#         id1=int(input('id пользователя'))
#         def funcone(id,):
#             cortegh=(id,)
#             conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
#
#             cursor=conn.cursor()
#
#             cursor.execute("DELETE FROM Pfonetel WHERE id=%s",cortegh)
#
#             conn.commit()
#             conn.close()
#             cursor.close()
#         funcone(id1)
#     elif info ==6:
#         id1=int(input('id пользователя'))
#         a=input('Имя пользователя')
#         b=input('email пользователя')
#         f=input('телефон пользователя')
#         def funcone(id,a,b,f):
#             cortegh=(id,a,b,f)
#             conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')
#
#             cursor=conn.cursor()
#
#             cursor.execute("SELECT * FROM Pfonetel WHERE id=%s OR name=%s OR email=%s OR numphone=%s",cortegh)
#             print(cursor.fetchall())
#
#             conn.commit()
#             conn.close()
#             cursor.close()
#         funcone(id1,a,b,f)



while True:
    info = int(input(f'1.Создать таблицу'
                         f'2.Добавить пользователя\n'
                         f'3.Изменить значения пользователя\n'
                         f'4.Изменить номер\n'
                         f'5.Удалить пользователя\n'
                         f'6.Вывести всю информацию'))
    if info == 1:
        a=input('Имя пользователя')
        b=input('email пользователя')
        f=input('телефон пользователя')
        def funcone():
            conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')

            cursor=conn.cursor()

            cursor.execute("CREATE TABLE Pfonetel"
                           "(id SERIAL PRIMARY KEY,"
                           "name VARCHAR(50),"
                           "email VARCHAR(20),"
                           "numphone VARCHAR(30) )")
            conn.commit()
            conn.close()
            cursor.close()
        funcone()


    elif info ==2:
        a=input('Имя пользователя')
        b=input('email пользователя')
        f=input('телефон пользователя')
        def funcone(a,b,f):
            cortegh=(a,b,f)
            conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')

            cursor=conn.cursor()

            cursor.execute("INSERT INTO Pfonetel(name,email,numphone) VALUES (%s,%s,%s)",cortegh)


            conn.commit()
            conn.close()
            cursor.close()
        funcone(a,b,f)
    elif info ==3:
        id1=int(input('id пользователя'))
        a=input('Имя пользователя')
        b=input('email пользователя')
        f=input('телефон пользователя')
        def funcone(id,a,b,f):
            cortegh=(a,b,f,id)
            conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')

            cursor=conn.cursor()

            cursor.execute("UPDATE Pfonetel SET name=%s,email = %s,numphone=%s WHERE id=%s",cortegh)

            conn.commit()
            conn.close()
            cursor.close()
        funcone(id1,a,b,f)
    elif info ==4:
        id1=int(input('id пользователя'))
        f=input('телефон пользователя')
        def funcone(id,f):
            cortegh=(id,f)
            conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')

            cursor=conn.cursor()

            cursor.execute("UPDATE Pfonetel SET numphone=%s WHERE id=%s",cortegh)

            conn.commit()
            conn.close()
            cursor.close()
        funcone(id1,f)
    elif info ==5:
        id1=int(input('id пользователя'))
        def funcone(id,):
            cortegh=(id,)
            conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')

            cursor=conn.cursor()

            cursor.execute("DELETE FROM Pfonetel WHERE id=%s",cortegh)

            conn.commit()
            conn.close()
            cursor.close()
        funcone(id1)
    elif info ==6:
        id1=int(input('id пользователя'))
        a=input('Имя пользователя')
        b=input('email пользователя')
        f=input('телефон пользователя')
        def funcone(id,a,b,f):
            cortegh=(id,a,b,f)
            conn = psycopg2.connect(dbname='testdb1', user='postgres',password='user',host='127.0.0.1',port='5432')

            cursor=conn.cursor()

            cursor.execute("SELECT * FROM Pfonetel WHERE id=%s OR name=%s OR email=%s OR numphone=%s",cortegh)
            print(cursor.fetchall())

            conn.commit()
            conn.close()
            cursor.close()
        funcone(id1,a,b,f)
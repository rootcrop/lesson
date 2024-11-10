import time, random
import sqlite3

start_time=time.time()
connection = sqlite3.connect('not_telegram.db')
cursor=connection.cursor()

#cursor.execute('DROP TABLE Users')  # удаляем таблицу
cursor.execute('''                  /* метод execute исполняет SQL команды                          */
CREATE TABLE IF NOT EXISTS Users(   /* IF NOT EXISTS        проверка чтобы случайно не стереть      */
id INTEGER PRIMARY KEY,             /* ключевые команды пишутся капсом                              */
username TEXT NOT NULL,             /* названия таблиц пишутся 1я с большой буквы Users             */
email TEXT NOT NULL,                /* поля пишутся маленькими буквами                              */
age INTEGER,                        /* тип целый INTEGER, текстовый TEXT, не пустое поле NOT NULL   */
balance  INTEGER NOT NULL
) ''')

# заполняем базу
#for i in range (1,11):
#    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',(f'User{i}',f'example{i}@gmail.com', f'{i*10}', '1000'))

## Обновите balance у каждой 2ой записи начиная с 1ой на 500:
#for i in range (1,10,2):
#    cursor.execute('UPDATE Users SET balance  = ? WHERE id = ?', (500,i))

## Удалите каждую 3ую запись в таблице начиная с 1ой:
#for i in range (1,11,3):
#    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))   # , нужна для кортежа

## Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60
#cursor.execute('SELECT username,email,age,balance FROM Users WHERE age != ?', (60,))
#users=cursor.fetchall()
#for u in users:
#    print(u)

## Удаление пользователя с id=6
cursor.execute('DELETE FROM Users WHERE id == ?',(6,))

## Подсчёт кол-ва всех пользователей
all=cursor.execute('SELECT COUNT(*) FROM Users').fetchall()[0][0]   # считаем всех, берем из кортежа [0][0]

## Подсчёт суммы всех балансов
all_balance=cursor.execute('SELECT SUM(balance) FROM Users')
all_balance=all_balance.fetchall()[0][0]

print(all_balance/all)

connection.commit()
connection.close()

print(f'время исполнения: {time.time()-start_time:,.3f}'.replace(',', ' '))     # разделение 3х сначений пробелом
import time, random
import sqlite3

start_time=time.time()
connection = sqlite3.connect('not_telegram.db')
cursor=connection.cursor()        # "объект" для взаимодействия с базой данных

cursor.execute('DROP TABLE Users')  # удаляем таблицу

cursor.execute('''                  /* метод execute исполняяет SQL команды                         */
CREATE TABLE IF NOT EXISTS Users(   /* IF NOT EXISTS        проверка чтобы случайно не стереть      */
id INTEGER PRIMARY KEY,             /* ключевые команды пишутся капсом                              */
username TEXT NOT NULL,             /* названия таблиц пишутся 1я с большой буквы Users             */
email TEXT NOT NULL,                /* поля пишутся маленькими буквами                              */
age INTEGER,                        /* тип целый INTEGER, текстовый TEXT, не пустое поле NOT NULL   */
balance  INTEGER NOT NULL
) ''')

for i in range (1,11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',(f'User{i}',f'example{i}@gmail.com', f'{i*10}', '1000'))

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
for i in range (1,10,2):
    cursor.execute('UPDATE Users SET balance  = ? WHERE id = ?', (500,i))

# Удалите каждую 3ую запись в таблице начиная с 1ой:
for i in range (1,11,3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))   # , нужна для кортежа

cursor.execute('SELECT username,email,age,balance FROM Users WHERE age != ?', (60,))
users=cursor.fetchall()
for u in users:
    print(u)

connection.commit()
connection.close()

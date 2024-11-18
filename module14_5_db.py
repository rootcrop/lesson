import  sqlite3, time

# скелет подключения
#connection=sqlite3.connect('module14_db.db'); cursor=connection.cursor()
#connection.commit(); connection.close()

# пишем простой CRUD/ORM   urban-university.ru/members/courses/course999421818026/20240202-0000lekcia-napisanie-primitivnoj-orm-923022744006

connection=sqlite3.connect('module14_5_db.db')
cursor=connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT,
username TEXT,
first_name TEXT,
block INT       /* заблокирован ли юзер */
) ''')

def add_user(user_id, username, first_name):
    check_name=cursor.execute('SELECT * FROM Users WHERE id=?', (user_id,))  # ищем есть ли в базу уже user с id
    if check_name.fetchone() is None:       # если такого пользователя еще нет добавляем
        cursor.execute(f'''
        INSERT INTO Users VALUES('{user_id}','{username}','{first_name}',0)     /* INSERT INTO Users VALUES('','') */
        ''')
        connection.commit()

def show_users():
    users=cursor.execute('SELECT * FROM Users')
    #for a in all: print(a)
    message=''
    for user in users:
        message+=f"{user[0]} @{user[1]} {user[2]} {user[3]} \n"
    connection.commit()
    return message

def show_stat():
    count_users=cursor.execute('SELECT COUNT(*) FROM Users').fetchone()[0]
    connection.commit()
    return count_users

def add_to_block(input_id):
    cursor.execute(f"UPDATE Users SET block = ? WHERE id = ?", (1, input_id))
    connection.commit()

def remove_block(input_id): # обновляем таблицу Users, ставим значение block, где id
    cursor.execute(f"UPDATE Users SET block = ? WHERE id = ?", (0, input_id))
    connection.commit()

def check_block(user_id):
    user=cursor.execute(f"SELECT block FROM Users WHERE id = {user_id}").fetchone()
    connection.commit()
    return user[0]


#add_to_block(1)
#add_user ('2','Max', '1st')
#print( show_users() )
#print(show_stat())
#print(check_block(0) )
#remove_block(1)
#print(check_block(2) )


# github.com/rootcrop/lesson/blob/main/module14_1_sql.py

#cursor.execute('DROP TABLE IF EXISTS Users')  # удаляем таблицу

#cursor.execute('''                  /* метод execute исполняет SQL команды                          */
#CREATE TABLE IF NOT EXISTS Users(   /* IF NOT EXISTS        проверка чтобы случайно не стереть      */
#id INTEGER PRIMARY KEY,             /* ключевые команды пишутся капсом                              */
#username TEXT NOT NULL,             /* названия таблиц пишутся 1я с большой буквы Users             */
#email TEXT NOT NULL,                /* поля пишутся маленькими буквами                              */
#age INTEGER,                        /* тип целый INTEGER, текстовый TEXT, не пустое поле NOT NULL   */
#balance  INTEGER NOT NULL
#) ''')

#for i in range (1,11): cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',(f'User{i}',f'example{i}@gmail.com', f'{i*10}', '1000'))

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:    #for i in range (1,10,2): cursor.execute('UPDATE Users SET balance  = ? WHERE id = ?', (500,i))
# Удалите каждую 3ую запись в таблице начиная с 1ой:            #for i in range (1,11,3): cursor.execute('DELETE FROM Users WHERE id = ?', (i,))   # , нужна для кортежа

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60
#cursor.execute('SELECT username,email,age,balance FROM Users WHERE age != ?', (60,))
#users=cursor.fetchall()
#for u in users: print(u)
#connection.commit(); connection.close()

connection.commit(); connection.close()

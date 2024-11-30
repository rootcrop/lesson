import  sqlite3

from numpy.ma.core import count

# шаблон/скелет подключения
#connection=sqlite3.connect('module14_db.db')
#cursor=connection.cursor()
#    cursor.execute('''
#     ) ''')
#connection.commit(); connection.close()
db_file='module14_52.db'
connection=sqlite3.connect(db_file)
cursor=connection.cursor()

def connect ():
    connection=sqlite3.connect(db_file)
    cursor=connection.cursor()
    return cursor

# инициализируем базу User: id / username / email / age / balance
def initiate_db_users():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INT INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    ) ''')

def add_user(username, email, age):
    count_all= cursor.execute('SELECT COUNT(*) FROM Users').fetchone()[0]
    if is_included(username) is None:       # если такого пользователя еще нет добавляем
        cursor.execute(f'''
        INSERT INTO Users VALUES('{count_all+1}', '{username}', '{email}','{age}', 1000)     /* INSERT INTO Users VALUES('','') */
        ''')
        connection.commit()
    else:
        return False

def is_included(username):
    count_all = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    return count_all.fetchone()     # если ничего не найдено то резудьтат None

# инициализируем базу Products: id / title / description / price / image_name
def initiate_db_products():
    cursor.execute('''               
    CREATE TABLE IF NOT EXISTS Products(
    id INT INTEGER PRIMARY KEY,  
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL,           /* цена, не пустая not empty */
    image_name TEXT
    ) ''')

# заполняем Products : title / description / imagename / price
def add_db_products(title, description, imagename, price=1000 ):
    # insert ver1
    #cursor.execute( 'INSERT INTO Products (title,description,price) VALUES (?,?,?)',
    #    ('Product 5','description 5','555')    )

    #insert ver2
    #product_name='Загадочный мир';
    #cursor.execute(f''' INSERT INTO Products VALUES('1', '{product_name}','Игра в жанре приключения, где игрок исследует таинственный мир, разгадывает головоломки и раскрывает секреты','111','module14_32_image1.jpg') ''')

    # insert ver3
    #sql = """INSERT INTO Products
    #    (title, description, price, image_name)
    #    VALUES (?,?,?,?)"""
    #cursor.execute(sql, ('название', 'описание','111','image.jpg'))

    #txt1='Игра в жанре головоломки, где игрок должен перемещать кубики, чтобы создавать различные фигуры и решать сложные задачи.'
    #cursor.execute(sql, ('3Д кубики',
    #                     f'{txt1}',
    #                     '444', 'module14_32_image4.jpg'))
    count_all = cursor.execute('SELECT COUNT(*) FROM Products').fetchone()[0]
    sql = """INSERT INTO Products
            (id, title, description, price, image_name)
            VALUES (?,?,?,?,?)"""
    cursor.execute(sql, (
                        f'{count_all+1}',
                        f'{title}',
                        f'{description}',
                        f'{imagename}',
                        f'{price}'))
    connection.commit()

def get_all_products():
    cursor.execute('''    
    SELECT * FROM Products    
    ''')
    products = cursor.fetchall()
    return products

def add_user0(user_id, username, first_name):
    check_name=cursor.execute('SELECT * FROM Users WHERE id=?', (user_id,))  # ищем есть ли в базу уже user с id
    if check_name.fetchone() is None:       # если такого пользователя еще нет добавляем
        cursor.execute(f'''
        INSERT INTO Users VALUES('{user_id}','{username}','{first_name}',0)     /* INSERT INTO Users VALUES('','') */
        ''')
        connection.commit()

#initiate_db()
#insert_db()
#all_products=get_all_products()
#print( add_user('Masha4', 'mamasha@gmail.com', '33') )
#for a in all_products: print(a)

#add_db_products('Загадочный мир', 'Игра в жанре приключения, где игрок исследует таинственный мир, разгадывает головоломки и раскрывает секреты', 'module14_32_image1.jpg', 9)

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


#initiate_db_users()
#add_user('Alex1', 'alex@qqq.qq', 16)

#initiate_db_products ()
#add_db_products('Slow vibe', 'move slow under music', 'image2.jpg', 1001 )
#print( get_all_products () )

#connection.commit(); connection.close()

#print(len(get_all_products()))     # количество продуктов

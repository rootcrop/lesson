import  sqlite3
# шаблон/скелет подключения
#connection=sqlite3.connect('module14_db.db')
#cursor=connection.cursor()
#    cursor.execute('''
#
#     ) ''')
#connection.commit(); connection.close()

connection=sqlite3.connect('module14_db.db')
cursor=connection.cursor()

def connect ():
    connection=sqlite3.connect('module14_db.db')
    cursor=connection.cursor()
    return cursor

''' функция initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса. 
    таблица должна содержать следующие поля:
        id - целое число, первичный ключ
        title(название продукта) - текст (не пустой)
        description(описание) - текст
        price(цена) - целое число (не пустой)   '''

def initiate_db():          # создаем Products
    cursor.execute('''               
    CREATE TABLE IF NOT EXISTS Products(
    id INT INTEGER PRIMARY KEY,  
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL,           /* цена, не пустая not empty */
    image_name TEXT
    ) ''')

def insert_db():            # заполняем Products
    # insert ver1
    #cursor.execute( 'INSERT INTO Products (title,description,price) VALUES (?,?,?)',
    #    ('Product 5','description 5','555')    )

    #insert ver2
    #product_name='Загадочный мир';
    #cursor.execute(f''' INSERT INTO Products VALUES('1', '{product_name}','Игра в жанре приключения, где игрок исследует таинственный мир, разгадывает головоломки и раскрывает секреты','111','module14_32_image1.jpg') ''')

    # insert ver3
    sql = """INSERT INTO Products
        (title, description, price, image_name) 
        VALUES (?,?,?,?)"""
    #cursor.execute(sql, ('название', 'описание','111','image.jpg'))

    txt1='Игра в жанре головоломки, где игрок должен перемещать кубики, чтобы создавать различные фигуры и решать сложные задачи.'
    cursor.execute(sql, ('3Д кубики',
                         f'{txt1}',
                         '444', 'module14_32_image4.jpg'))
    connection.commit()

def get_all_products():
    cursor.execute('''    
    SELECT * FROM Products    
    ''')
    products = cursor.fetchall()
    return products

def add_user(user_id, username, first_name):
    check_name=cursor.execute('SELECT * FROM Users WHERE id=?', (user_id,))  # ищем есть ли в базу уже user с id
    if check_name.fetchone() is None:       # если такого пользователя еще нет добавляем
        cursor.execute(f'''
        INSERT INTO Users VALUES('{user_id}','{username}','{first_name}',0)     /* INSERT INTO Users VALUES('','') */
        ''')
        connection.commit()

#initiate_db()
#insert_db()
#all_products=get_all_products()
#for a in all_products: print(a)



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



#connection.commit(); connection.close()
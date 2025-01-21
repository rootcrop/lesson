# pip install fastapi, uvicorn      # run: python3 -m uvicorn module16_3:app    # http://127.0.0.1:8000/docs
from fastapi import FastAPI, Path   # Path для проверки переменных
from typing import Annotated        # Annotated для проверки переменных (с версии 3.9)
from fastapi import HTTPException
# основные запросы FastAPI
# Get       это обычно адрес в строке ?переменная=значение   или ?question=answer
# Post      это формы - оформить заказ в магазин
# Put       обновить, заменить
# Delete

app = FastAPI()                                 # инициализация приложения FastAPI
user_db = {'1': 'Имя: Дэн, возраст: 18', '2': 'Имя: Саша, возраст: 22', }    # первичная БД

# база данных:      Create, Read,   Edit,   Update, Delete
# типы запросов     post    get             put     delete

@app.get('/users')
async def get_users() -> dict:
    return user_db

@app.post('/user/{username}/{age}')                     # добавление через метод POST
async def add_user (
        username: Annotated[str, Path(min_length=4, max_length=20, regex="^[a-zA-Z0-9А-Яа-я0-9_-]+$", description='Enter username 4-20 letters, in english or cyrillic letters, digits, "_", "-"')],
        age: Annotated[int, Path(ge=1, le=100, description='Enter age')]
        ) -> str:
    current_index = str(int(max(user_db, key=int))+1)   # находим последнее максимальное значение в базе и +1
    user_db [current_index]= f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registered'

                                                # Метод PUT заменяет существующую запись новой, по её ID.
@app.put('/user/{user_id}/{username}/{age}')    # Update / создаем асинхронную функцию обновления сообщения
async def update_user (
        user_id: Annotated[int, Path(ge=1, le=1000)],
        username: Annotated[str, Path(min_length=4, max_length=20, regex="^[a-zA-Z0-9А-Яа-я0-9_-]+$",
            description='Enter username 4-20 letters, in english or cyrillic letters, digits, "_", "-"')],
        age: Annotated[int, Path(ge=1, le=100, description='Enter age')]):
    try:
        # чтобы получить доступ к словарю переводим int в str
        user_db[str(user_id)] = f'Имя: {username}, возраст: {age}'    # обновляем сообщение
        msg=f'The user {user_id} is updated'
    except:
        raise HTTPException (status_code=404, detail='user ID not found')  # не находим: выводим 404
    return msg

@app.delete('/user/{user_id}')        # Delete / создаем асинхронную функцию удаления конкретного юзера, с проверкой на цифры
async def delete_messages (user_id: Annotated[str, Path(min_length=1, max_length=4, regex="^[0-9]+$")]) -> str:     # или regex = /^\d+$/;
    try:
        user_db.pop(user_id)          # удаляем сообщение с message_id
    except:
        raise HTTPException(status_code=404, detail='user ID not found')  # не находим: выводим 404
    return f'user with ID {user_id} was delited'

@app.delete('/')
async def delete_all_users () -> str:
    user_db.clear()
    return 'all users deleted'

@app.get('/')                   # маршрутизация / routing
async def hellow_msg() -> dict: # на вход функции ничего нет, на выходы проверяем, что это словарь
    return {"message":"hellow"}

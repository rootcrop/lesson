# pip install fastapi, uvicorn
# run:      python -m uvicorn module_16_1:app
# server:   http://127.0.0.1:8000/docs

from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel, Field

''' Задача "Аннотация и валидация":
Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated:
'/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id, для которого необходимо написать следующую валидацию:
    Должно быть целым числом
    Ограничено по значению: больше или равно 1 и меньше либо равно 100.
    Описание - 'Enter User ID'
    Пример - '1' (можете подставить свой пример не противоречащий валидации)

'/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту, принимает аргументы username и age, для которых необходимо написать следующую валидацию:
    username - строка, age - целое число.
    username ограничение по длине: больше или равно 5 и меньше либо равно 20.
    age ограничение по значению: больше или равно 18 и меньше либо равно 120.
    Описания для username и age - 'Enter username' и 'Enter age' соответственно.
    Примеры для username и age - 'UrbanUser' и '24' соответственно. (можете подставить свои примеры не противоречащие валидации) '''

app = FastAPI()     # инициализация приложения

# маршрутизация // routing
@app.get('/')
async def welcome() -> str:     # функция welcome -> возвращает str
    return "Главная страница"   # FastAPI проверяет на соотвествие типа данных и преобразует словарь в JSON

@app.get("/user/{user_id}") #  gt (greater than), ge (greater than or equal), lt (less than), и le (less than or equal)
async def user ( user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')] ) -> str:     # возвращаем str
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}")                      # http://127.0.0.1:8000/user/alex/22
async def user (username:  Annotated[str, Path(description='Enter username')],
                age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get('/user/admin')
async def admin() -> str:
    return 'Вы вошли как администратор'

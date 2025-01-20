# pip install fastapi, uvicorn
# run:      python -m uvicorn module_16_1:app
# server:   http://127.0.0.1:8000/docs

from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel, Field
app = FastAPI()     # инициализация приложения

# маршрутизация // routing
@app.get('/')
async def welcome() -> dict:                # функция welcome -> возвращает словарь
    return {"message":"Главная страница"}   # FastAPI проверяет на соотвествие типа данных и преобразует словарь в JSON

@app.get("/user/{user_id}") #  gt (greater than), ge (greater than or equal), lt (less than), и le (less than or equal)
async def user ( user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')] ) -> str:
    return f"Вы вошли как пользователь № {user_id}"     # возвращаем str

@app.get("/user/{username}/{age}")                      # http://127.0.0.1:8000/user/alex/22
async def user (username:  Annotated[str, Path(description='Enter username')],
                age: Annotated[int, Path(ge=18, le=120, description='Enter age')]):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get('/user/admin')
async def admin() -> list:      # функция  admin -> возвращает словарь
    return ["message","Вы вошли как администратор"]     # список также будет преобразован в JSON-массив.

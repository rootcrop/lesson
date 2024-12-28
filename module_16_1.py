# pip install fastapi, uvicorn
# run:      python3 -m uvicorn module_16_1:app
# server:   http://127.0.0.1:8000/docs

from fastapi import FastAPI
app = FastAPI()     # инициализация приложения

# маршрутизация // routing
@app.get('/')
async def welcome() -> dict:    # функция welcome -> возвращает словарь
    return {"message":"Главная страница"}   # FastAPI проверяет на соотвествие типа данных и преобразует словарь в JSON

@app.get('/user/admin')
async def admin() -> list:      # функция  admin -> возвращает словарь
    return ["message","Вы вошли как администратор"]     # список также будет преобразован в JSON-массив.

@app.get("/user/{user_id}")                             # http://127.0.0.1:8000/user/222
async def user (user_id:int) -> str:
    return f"Вы вошли как пользователь № {user_id}"     # возвращаем str

@app.get("/user/")                                      # http://127.0.0.1:8000/user?username=sasa&age=33
async def user2 (username: str, age: int):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}  # возвращаем без проверок

@app.get("/user/{username}/{age}")                      # http://127.0.0.1:8000/user/alex/22
async def user3 (username: str, age: int):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

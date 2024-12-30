# pip install fastapi, uvicorn              # urban-university.ru/members/courses/course999421818026/20240215-0000lekcia-osnovy-fast-api-918957519537
# run: python3 -m uvicorn main_fastApi:app  # http://127.0.0.1:8000/docs

from fastapi import FastAPI, Path   # Path для проверки переменных
from typing import Annotated        # Annotated для проверки переменных (с версии 3.9)

# основные запросы FastAPI
# Get       это обычно адрес в строке ?переменная=значение   или ?question=answer
# Post      это формы - оформить заказ в магазин
# Put       обновить, заменить
# Delete

app = FastAPI()     # инициализация приложения FastAPI

# маршрутизация _ корень // routing
@app.get('/')       # как в чат_ботах, через декоратор: если получаем запрос на / отрабатываем нижестоящую функцию
async def welcome() -> dict:    # функция welcome -> возвращает словарь
    return {"message":"hellow world!"}   # возвращаем словарь

# маршрутизация _ user
@app.get("/user/{user_id}")
# gt (greater than > ), ge (greater than or equal >= ), lt (less than < ), и le (less than or equal =< )
async def user (user_id: int = Path(ge=1, le=100, description='Enter User ID')) -> dict:
    return {"message" : f"user_id : {user_id}"}

# маршрутизация _ user0_username_age _ проверка через Path
@app.get("/user0/{username}/{age}")
# gt (greater than > ), ge (greater than or equal >= ), lt (less than < ), и le (less than or equal =< )
async def user0 (username: str = Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9А-Яа-я0-9_-]+$", description='Enter username in english or cyrillic letters, digits, "_", "-"'),
                age: int = Path(ge=18, le=120, description='Enter age')
                ) -> dict:
    return {"message" : f"user_id : {username}, age: {age}"}

# маршрутизация _ user_username_age _ проверка через Annotated
@app.get("/user/{username}/{age}")
async def user (username: Annotated[str, Path(min_length=5, max_length=20, regex="^[a-zA-Z0-9А-Яа-я0-9_-]+$", description='Enter username in english or cyrillic letters, digits, "_", "-"')],
                age: Annotated[int, Path(ge=18, le=120, description='Enter age')]
                ) -> dict:
    return {"message" : f"user_id : {username}, age: {age}"}

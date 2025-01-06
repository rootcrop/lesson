from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List                 # List: Тип-подсказка для списков.

app = FastAPI()     # создаем экземпляр FastAPI application

# BaseModel: Все модели Pydantic наследуются от BaseModel
# BaseModel: Класс Pydantic, используемый для определения моделей данных (схем) для валидации запросов и ответов.
# задаем типы данных, чтобы FastAPI автоматически проверял их соответствие и типизировал выходные данные.
# Field: Используется для добавления ограничений или метаданных к полям в моделях Pydantic.
class User (BaseModel):
    # gt(greater than >)  ge(greater than or equal >=)  lt(less than <)  le(less than or equal =<)
    id:         int = Field(..., gt=0, lt=1000) # Параметр Field ограничивает поле длинной >0 и <1000
    username:   str = Field(..., min_length=3,max_length=10, description="Имя пользователя")
    age:        int = Field(..., ge=18, lt=99)

# Инициализируем список пользователей с явной типизацией
# указываем тип users как List[User], FastAPI проверяет каждый объект в users на соответствие модели User
users: List[User] = [   User(id=1, username="Alex", age=22),
                        User(id=2, username="Malex", age=44)    ]

# Метод GET используется для получения данных с сервера
@app.get("/users", response_model=List[User])   # response_model: проверял тип данных возвращаемых клиенту
async def get_all_users():
    return users                                      # просто возвращаем ранее список users

# Создание новго пользователя, метод POST позволяет отправлять данные на сервер для создания новой задачи
# в реальном приложении нужна дополнительная проверка (например) на уникальность (почты и телефона)
@app.post("/users/{username}/{age}", response_model=User)
async def create_user(user: User):
    new_id = max((u.id for u in users), default=0) + 1
    new_user = User (id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user

# Обновление существующего пользователя (метод PUT)
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, username:str, age:int):
    for u in users:
        if u.id == user_id:
            u.username = username
            u.age = age
            return u
    # HTTPException: Используется для вызова исключений с определенными HTTP-кодами и сообщениями об ошибках.
    raise HTTPException(status_code=404, detail="User was not updated")

# Удаление пользователя (метод DELETE)
@app.delete("/user/{user_id}", response_model=dict) # возвращаем словарь с сообщением об удалении
async def delete_task(user_id: int):
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return {"detail": "пользователь удален"}
    raise HTTPException(status_code=404, detail="User was not found")

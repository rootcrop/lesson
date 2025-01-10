from fastapi import FastAPI, status, Body, HTTPException, Form, Request   # Request это запрос
from module16_5_pydantic import Message, messages_db
from pydantic import BaseModel
from typing import List
# pip install jinja2                            # шаблонизатор jinja2   в html вставляем {{user.username}}
from fastapi.templating import Jinja2Templates  # для подключения директории с шаблонами
from fastapi.responses import HTMLResponse      # HTMLResponse это ответ

app = FastAPI()
templates= Jinja2Templates(directory='templates3')

class User(BaseModel):
    id: int
    username: str
    age: int = None

users_db: List[User] = [    User(id=0, username="Alex", age=22),
                            User(id=1, username="Malex", age=33)    ]

@app.get("/")
def get_all_messages(request: Request) -> HTMLResponse: # получаем request, а возвращаем не list а HTMLResponse
    """
    выводим всех пользователей //
    в шаблон users.html возвращаем список users >> логическиий if в user.html определит вывод нужного блока //
    return: templates.TemplateResponse('users.html' ...
    """
    print(users_db)
    return templates.TemplateResponse('users.html',{'request': request, 'users': users_db}) # возвращаем несколько messages, if в message.html определит вывод блока

@app.post("/user")
def create_user(user: User) -> str:     # т.к. выводим просто надпись об удачном создании пользователя
    """
    добавляем пользователя через админку /docs
    """
    user.id = max((u.id for u in users_db), default=0) + 1
    users_db.append(user)
    return f"User created!"

@app.get(path="/user/{user_id}")
def get_user(request: Request, user_id: int) -> HTMLResponse:
    '''
    выводим пользователя //
    в шаблон user.html возвращаем одного user >> логическиий if в user.html определит вывод нужного блока
    return: templates.TemplateResponse('users.html' ...
    '''
    try:
        id = next((index for index, user in enumerate(users_db) if user.id == user_id), -1)         # находим индекс элемента в списке
        return templates.TemplateResponse('users.html',{'request': request, 'user': users_db[id]})
    except IndexError:
        raise HTTPException(status_code=404, detail="user not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> str:
    '''
    удаляем конкретного пользователя
    '''
    try:
        id = next((index for index, user in enumerate(users_db) if user.id == user_id), -1)  # находим индекс элемента в списке
        users_db.pop(id)
        return f"User ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/")
def delete_users_all() -> str:
    '''
    удаляем всех пользователей
    '''
    users_db.clear()
    return "All users deleted!"

@app.put("/user/{user_id}/{username}/{age}")
def update_message(user_id: int, username: str, age:int ) -> str:
    '''
    редактируем-обновляем данные пользователя
    '''
    try:
        id = next((index for index, user in enumerate(users_db) if user.id == user_id), -1)         # находим индекс элемента в списке
        edit_user = users_db[id]
        edit_user.username = username
        edit_user.age = age
        return f"user updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="user not found")

@app.post("/", status_code=status.HTTP_207_MULTI_STATUS)   # post запрос посылаем на "/" в message.html это <form method="post" action="/">
def create_user(request: Request, user_name: str = Form(), user_age: str = Form()) -> HTMLResponse:
    '''
    добавляем user через html форму
    '''
    if users_db:
        user_id = max((user.id for user in users_db if user.id is not None), default=0)+1
    else:
        user_id=0
    users_db.append( User(id=user_id, username=user_name, age=int(user_age)) )
    return templates.TemplateResponse('users.html',{'request': request, 'users': users_db})

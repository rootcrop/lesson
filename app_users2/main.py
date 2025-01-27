# проект app_users          user with tasks
# app_users                 папка проекта
# app_users/__init__.py     файл init, нужен для импорта из *.py файлов
# app_users/main.py         основной запускаемый файл   #app_users> python -m uvicorn main:app
# app_users/schemas.py      модели(схемы) pydantic проверяющие тип атрибутов класса
# app_users/routers/user    пути для роутера и функции обработки пользователя
# app_users/routers/task    пути для роутера и функции обработки задач

from fastapi import FastAPI
from routers import user, task

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message":"Welcome to Taskmanager"}

app.include_router(user.router)     # подключаем созданные модели
app.include_router(task.router)
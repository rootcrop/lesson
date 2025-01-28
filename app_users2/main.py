# проект app_users2          user with tasks
# app_users2                 папка проекта
# app_users2/__init__.py     файл init, нужен для импорта из *.py файлов
# app_users2/main.py         основной запускаемый файл   #app_users> python -m uvicorn main:app
# app_users2/schemas.py      модели(схемы) pydantic проверяющие тип атрибутов класса
# app_users2/routers/user    пути для роутера и функции обработки пользователя
# app_users2/routers/task    пути для роутера и функции обработки задач

from fastapi import FastAPI
from routers import user, task

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message":"Welcome to Taskmanager"}

app.include_router(user.router)     # подключаем созданные модели
app.include_router(task.router)

#
# 1     alembic init app_users2/migrations    # создаем папку миграций с настройками
#

# файл alembic.ini                      # настройки куда сохранять базы данных для миграции
# script_location = app_users2/migrations
# sqlalchemy.url = sqlite:///taskmanager.db

# файл env.py                           # настройки сохранения нужных объектов проекта
'''
###target_metadata = None
#2  указали какие данные надо подключать
from app_users2.backend.udb import Base             # это наша базовая структура
from app_users2.models.category import Category
from app_users2.models.products import Product
target_metadata = Base.metadata                     '''

# файл backend/udb.py
# engine = create_engine('sqlite:///taskmanager.db', echo=True) # название файлы БД должно совпадать в alembic.ini

#
# 2
#
#alembic revision --autogenerate -m "first migration"   # в директории versions должна появится пустая ДБ с версия миграции и база данных

#
# 3
#
# alembic upgrade head          # устанавливаем последнюю версию миграции


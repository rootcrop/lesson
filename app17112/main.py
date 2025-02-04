from fastapi import FastAPI
from app17112.routers import task, user

app1 = FastAPI()
app1.include_router(task.router)
app1.include_router(user.router)

@app1.get('/')
async def welcome():
    return {"message": "taskmanager"}


# uvicorn app17112.main:app1                                # запуск uvicorn

# alembic init app17112/migrations                          # инициализация миграций
# alembic revision --autogenerate -m "first migration"      # создание первой миграции
# alembic upgrade head                                      # обновление версии

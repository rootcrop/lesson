from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify                             # для создания URL-совместимых строк (слагов) из обычных строк
from sqlalchemy import insert, select, update, delete   # для работы с базой данных
from sqlalchemy.orm import Session  # Импортируем класс Session для управления сессиями базы данных
from typing import Annotated        # аннотацию Annotated для добавления дополнительной информации к типам

from app17112.backend.db_depends import get_db          # Импортируем функцию get_db, которая предоставляет сессию базы данных, Функция get_db предоставляется через механизм зависимости Depends, что позволяет автоматически внедрять сессию базы данных в маршруты
from app17112.models import User                        # Импортируем модель User для взаимодействия с таблицей пользователей.
from app17112.schemas import CreateUser, UpdateUser     # Импортируем схемы CreateUser и UpdateUser для валидации данных.

router = APIRouter(prefix="/user", tags=["user"])       # Создаём новый роутер с префиксом /user и тегом user. Это позволяет группировать маршруты и управлять ими централизованно.
SessionAnnotated = Annotated[Session, Depends(get_db)]  # Annotated: Используется для добавления дополнительной информации к типу, SessionAnnotated указывает, что параметр должен быть типа Session и должен быть предоставлен функцией get_db через механизм зависимости Depends.


@router.get('/')                                        # @router.get('/') : Определяет маршрут GET-запроса по пути /user/
async def all_users(se: SessionAnnotated):              # Параметр se автоматически внедряется с помощью зависимости get_db, предоставляя сессию базы данных
    return se.scalars(select(User)).all()               # метод all возвращает список всех результатов, SQL-запрос выбора всех пользователей из таблицы User и возвращает их в виде списка

@router.get('/user_id')                                         # Определяем маршрут GET-запроса по пути /user/user_id
async def user_by_id(se: SessionAnnotated, user_id: int):       # параметр se внедряется с помощью зависимости get_db, параметр user_id передаётся как часть URL-запроса
    user = se.scalar(select(User).where(User.id == user_id))    # SQL-запрос для выбора пользователя с заданным id.
    if not user:        # Обработка Ошибок: Использование HTTPException позволяет отправлять пользователю информативные сообщения об ошибках с соответствующими кодами состояния
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User was not found')
    return user


@router.post('/create')
async def create_user(se: SessionAnnotated, user: CreateUser) -> dict:
    if se.scalar(select(User.username)                          # Метод scalars возвращает скалярные значения (одиночные объекты)
                   .where(User.username == user.username)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Duplicated username')
    user_dict = dict(user)
    user_dict['slug'] = slugify(user.username)
    se.execute(insert(User), user_dict)
    se.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}


@router.put('/update')
async def update_user(se: SessionAnnotated, user: UpdateUser, user_id: int) -> dict:
    if not se.scalar(select(User.id).where(User.id == user_id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User was not found')
    se.execute(update(User).where(User.id == user_id),
                 dict(user))
    se.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User has been updated successfully'}


@router.delete('/delete')
async def delete_user(se: SessionAnnotated, user_id: int) -> dict:
    if not se.scalar(select(User.id).where(User.id == user_id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User was not found')
    se.execute(delete(User).where(User.id == user_id))
    se.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User has been deleted successfully'}

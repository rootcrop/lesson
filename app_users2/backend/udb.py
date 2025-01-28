# sql ORM
from sqlalchemy import create_engine                        # минус: нет встроенных миграций
from sqlalchemy.orm import sessionmaker, DeclarativeBase    # для sql ORM
from sqlalchemy import Column, Integer, String              #

engine = create_engine('sqlite:///taskmanager.db', echo=True)       # движок для связи с ДБ
SesssionLocal = sessionmaker (bind=engine)                          # сессия связи с ДБ

class Base(DeclarativeBase):    # нужно для сопоставления классов моделей и таблиц БД
    pass

# для моделей делаем отдельную папку models

# этот пример класа, который строит необходимую БД (без написания SQL запроса)
"""
class User(Base):
    __tablename__ = 'user'
    id = Column (Integer, primary_key=True)     # автоматически заполняется
    username= Column (String)
    password = Column (String)
"""

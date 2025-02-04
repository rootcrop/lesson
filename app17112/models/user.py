from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import Column, Integer, String
from typing import List, Optional
from app17112.backend.db import Base


# Mapped[] и mapped_column аннотации являются частью нового API SQLAlchemy 2.0
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[Optional[str]]
    firstname: Mapped[Optional[str]]
    lastname: Mapped[Optional[str]]
    age: Mapped[Optional[int]]
    slug: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    tasks: Mapped[List['Task']] = relationship(back_populates='user')


# Column() вариант написания до 2.0 версии SQLAlchemy
'''
class User_(Base):
    __tablename__='users'
    __table_args__ = {"keep_existing": True}    #  аргумент указывает SQLAlchemy сохранять существующую таблицу, если она уже существует. Это может быть полезно при миграциях или при использовании существующей базы данных, но может привести к нежелательному поведению при изменении структуры таблиц

    id = Column (Integer, primary_key=True, index=True) #
    username = Column (String)
    firstname = Column (String)
    lastname = Column (String)
    age = Column (Integer)
    slug = Column(String, unique=True, index=True)
    tasks=relationship("Task", back_populates='user')   # связь один ко многим (в данном случае)
'''
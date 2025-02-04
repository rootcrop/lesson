from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship  # Mappe relationship
from typing import Optional
from app17112.backend.db import Base


#  Mapped[] и mapped_column это аннотации нового API SQLAlchemy 2.0
#  более типизированному и современному подходу к определению моделей
class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[Optional[str]]                                    # Optional[] поля могут быть None
    content: Mapped[Optional[str]]
    priority: Mapped[Optional[int]] = mapped_column(default=0)
    completed: Mapped[Optional[bool]] = mapped_column(default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))    #, nullable=False, index=True)
    slug: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    user: Mapped['User'] = relationship(back_populates='tasks')

# Column() старый стиль SQLAlchemy ORM версий до 2.0
'''
class Task_old(Base):
    __tablename__ = 'tasks'
    __table_args__ = {"keep_existing": True}                        # аргумент указывает SQLAlchemy сохранять существующую таблицу, если она уже существует. Это может быть полезно при миграциях или при использовании существующей базы данных.
    id = Column (Integer, primary_key=True, index=True)             # целое число, первичный ключ, с индексом
    title = Column (String)
    content = Column (String)
    priority = Column(Integer, default=0)                           # целое число, по умолчанию 0
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)   # целое число, внешний ключ на id из таблицы 'users', не NULL, с индексом
    slug = Column(String, unique=True, index=True)
    user = relationship('User', back_populates='tasks')     # объект связи(1k1) с таблицей с таблицей User, где back_populates='tasks'
'''
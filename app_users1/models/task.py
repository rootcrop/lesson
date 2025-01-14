from app_users1.backend.udb import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float     # ForeignKey указываем на другую ячейку для связи между таблицами
from sqlalchemy.orm import relationship
#from app_users1.models import user
from app_users1.models import *

class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {"keep_existing": True}
    id = Column (Integer, primary_key=True, index=True)             # целое число, первичный ключ, с индексом
    title = Column (String)
    content = Column (String)
    priority = Column(Integer, default=0)                           # целое число, по умолчанию 0
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)   # целое число, внешний ключ на id из таблицы 'users', не NULL, с индексом
    slug = Column(String, unique=True, index=True)
    user = relationship('User', back_populates='tasks')     # объект связи(1k1) с таблицей с таблицей User, где back_populates='tasks'

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))
from app_users1.backend.udb import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean     # ForeignKey указываем на другую ячейку для связи между таблицами
from sqlalchemy.orm import relationship
#from app_users1.models import task    # импорт одного класса модели в модуль с другим, чтобы таблицы были видны друг другу
from app_users1.models import *

class User(Base):
    __tablename__='users'
    __table_args__ = {"keep_existing": True}
    id = Column (Integer, primary_key=True, index=True) #
    username = Column (String)
    firstname = Column (String)
    lastname = Column (String)
    age = Column (Integer)
    slug = Column(String, unique=True, index=True)

    tasks=relationship("Task", back_populates='user')   # связь один ко многим (в данном случае)

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))
#print(CreateTable(Product.__table__))
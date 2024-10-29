from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

from bot1 import api_key
api=api_key.key

bot=Bot(token=api)                          # переменная bot будет хранить объект Bot с нашим токеном
dp=Dispatcher(bot, storage=MemoryStorage()) # объект диспатчер, в качестве аргументов наш бот, храним в памяти

@dp.message_handler(lambda message: message.text and 'hello' in message.text.lower())
async def hello_message(message):
    print('Hello message')

@dp.message_handler(commands=['start'.lower()])             # commands это команда на которую будем реагировать
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью')

@dp.message_handler()
async def all_message(message):                             # отрабатывает все что не отработало выше
    print('Введите команду /start, чтобы начать общение.')

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)


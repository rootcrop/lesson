# pip install aiogram==2.25.1
import logging
from aiogram import Bot, Dispatcher, executor   # types
from aiogram.contrib.fsm_storage.memory import MemoryStorage                #import asyncio
#from aiogram.dispatcher.filters.state import State, StatesGroup             #from aiogram.dispatcher import FSMContext
#from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton        # кнопки для каталога

# my custom import project
from module14_32_bot_config import *     # в config      настройка АПИ и цен
from module14_32_bot_keyboards import *  # в keyboards   вывод меню через клавиатуру
import module14_32_bot_texts as text     # в text        тексты для вывода информации, описание игр
# from module14_32_admin import *          # создаем небольшую админ панель : есть список пользователей, колв-во юзеров, блокировка\разблок юзеров
# from module14_32_db import *             # urban-university.ru/members/courses/course999421818026/20240201-0000lekcia-plan-napisania-adminpaneli-925364922666
from module14_4_crud_functions import *

api=API_KEY
bot=Bot(token=api)                          # переменная bot будет хранить объект Bot с нашим токеном
dp=Dispatcher(bot, storage=MemoryStorage()) # объект диспатчер, в качестве аргументов наш бот, храним в памяти

logging.basicConfig(level=logging.INFO)     # базовое логирование

get_all_products()  #print( get_all_products()[0][1] )
#connection.commit(); connection.close()

# Задача "Витамины для всех!":
# понадобится 3 диспетчера-хэндлера на комнады: старт, о нас, прейскурант
@dp.message_handler(commands=['start'])     # стартовый хэндлер, через диспетчер вызываем ответ на команду start
async def start(message):
    await message.answer(f'Добро пожаловать,{message.from_user.username}\n'+text.start, reply_markup=start_kb)

# кроме текста можно выводить фото, видео и                 файл
#message.answer_photo               #message.answer_video   #message.answer_file

@dp.message_handler(text='О нас')       # обработчик-диспетчер вызываем ответ на текст
async def info(message):
    with open('1.jpg','rb') as img:
        await message.answer_photo(img, text.about, reply_markup=start_kb)
    #await message.answer (text.about, reply_markup=start_kb)       # просто вывести текст "о нас"

@dp.message_handler(text='Стоимость')       # обработчик-диспетчер вызываем каталог
async def price(message):
    await message.answer ('Что вас интересует?', reply_markup=catalog_products)

# Измените функцию get_buying_list в модуле с Telegram-ботом, используя вместо обычной нумерации продуктов функцию get_all_products. Полученные записи используйте в выводимой надписи: "Название: <title> | Описание: <description> | Цена: <price>"
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range (0,4):
        await message.answer (f'Название: {get_all_products()[i][1]} \nОписание: {get_all_products()[i][2]} \nЦена: {get_all_products()[i][3]*100}')
        with open(f'module14_4_image{i}.jpg','rb') as img:
            await message.answer_photo(img)
    await message.answer ('Выберите продукт для покупки: ', reply_markup=catalog_products)

#3 Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
@dp.callback_query_handler(text='product_buying1')
async def send_confirm_message(call):
    await call.message.answer ('Вы успешно приобрели продукт #1 !')

@dp.callback_query_handler(text='product_buying2')
async def send_confirm_message(call):
    await call.message.answer ('Вы успешно приобрели продукт #2 !')

@dp.callback_query_handler(text='product_buying3')
async def send_confirm_message(call):
    await call.message.answer ('Вы успешно приобрели продукт #3 !')

@dp.callback_query_handler(text='product_buying4')
async def send_confirm_message(call):
    await call.message.answer ('Вы успешно приобрели продукт #4 !')

@dp.message_handler()                       # действует на все не сработавшее ранее
async def start (message):
    await message.answer( 'введите команду /start, чтобы начать общение' )

''' # шаблон-рыба-хэндлера 
@dp.callback_query_handler(text='')
async def buy_(call):
    await call.message.answer()
    await call.answer()     '''

@dp.callback_query_handler(text='medium')
async def buy_m(call):
    await call.message.answer(text.Mgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='big')
async def buy_l(call):
    await call.message.answer(text.Lgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='mega')
async def buy_x(call):
    await call.message.answer(text.Xlgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer('Что вас интересует?', reply_markup=catalog_products)
    await call.answer()

@dp.callback_query_handler(text='other')
async def buy_o(call):
    await call.message.answer(text.other, reply_markup=buy_kb)
    await call.answer()

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
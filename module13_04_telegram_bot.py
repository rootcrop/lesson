from aiogram import Bot, Dispatcher, executor   # types
from aiogram.contrib.fsm_storage.memory import MemoryStorage    #import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup #from aiogram.dispatcher import FSMContext
from bot1 import api_key

api=api_key.key
bot=Bot(token=api)                          # переменная bot будет хранить объект Bot с нашим токеном
dp=Dispatcher(bot, storage=MemoryStorage()) # объект диспатчер, в качестве аргументов наш бот, храним в памяти

class UserState(StatesGroup):               # делаем класс с 3 объектами
    age=State()
    growth = State()
    weight= State()

@dp.message_handler(commands=['calories'])  # ждем ввода calories
async def set_age(message):
    await message.answer('введите свой возраст: ')
    #print('введите свой возраст : ')
    await UserState.age.set()               # ждем ввода возраста c помощью метода set в атрибут age

@dp.message_handler(text=['calories'])      # ждем ввода calories
async def set_age(message):
    await message.answer('введите свой возраст: ')
    #print('введите свой возраст : ')
    await UserState.age.set()               # ждем ввода возраста c помощью метода set в атрибут age

@dp.message_handler(state=UserState.age)      # ждем ранее введенный возраст и записываем через update_data
async def set_growth(message, state):
    await state.update_data(age=message.text)   # записываем в age отправленное пользователем сообщение
    await UserState.age.set()                   # ждем ввода возраста c помощью метода set в атрибут age
    await message.answer('введите свой рост: ')
    #print('введите свой рост : ')
    await UserState.growth.set()                # ждем ввода роста

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('введите свой вес: ')
    #print('введите свой вес : ')
    await UserState.weight.set()                # ждем ввода веса

@dp.message_handler(state=UserState.weight)
async def set_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # упрощённая формула Миффлина-Сан Жеора         # для женщины: ВОО = 10 * вес(кг) + 6.25 * рост(см) – 4.92 * возраст – 161          # для мужчины: ВОО = 10 * вес(кг) + 6.25 * рост(см) – 4.92 * возраст + 5
    result1=10*int(data['weight']) + 6.25*int(data['growth'])-4.92*int(data['age'])-161 # fem
    result2=10*int(data['weight']) + 6.25*int(data['growth'])-4.92*int(data['age'])+5   # mal
    await message.answer(f' норма калорий для женщины: {result1:.1f} \nнорма калорий для мужчины: {result2:.1f} ')
    print(f' результаты для возраста {int(data["age"])}, роста {int(data["growth"])}, веса {int(data["weight"])} - ж: {result1}, п: {result2}')
    await state.finish()

@dp.message_handler(commands=['start'])     # text=['start']
async def start (message):
    #print('привет, я бот помогающий твоему здоровью, \nнапишите /calories для подсчета ежедневных калорий')
    await message.answer('привет!\nя бот помогающий твоему здоровью \n\nнапишите calories или нажмите /calories \nдля подсчета ежедневных калорий')

@dp.message_handler()                       # действует на все не сработавшее ранее
async def start (message):
    #print('введите команду /start, чтобы начать общение')
    await message.answer( 'введите команду /start, чтобы начать общение' )

# python 3.11.6 (3.11.8 тоже работает)      # aiogram 2.25 (лучше 3.9.9)    # https://docs.aiogram.dev/en/v2.25.1/
if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)

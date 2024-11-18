from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# стартовый хэндлер, через диспетчер вызываем ответ на команду /start
start_kb=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Регистрация'), KeyboardButton(text='О нас'), KeyboardButton(text='Стоимость')],
        [ KeyboardButton(text='Купить') ]
    ], resize_keyboard=True
)

# catalog_kb=ReplyKeyboardMarkup(
#    keyboard=[[ KeyboardButton(text='первый продукт в каталоге'), KeyboardButton(text='второй продукт в каталоге')]], resize_keyboard=True )

##2 Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4". У всех кнопок назначьте callback_data="product_buying"
catalog_products=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying1')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying2')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying3')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying4')]
    ])

catalog_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Средняя игра', callback_data='game_medium')],
        [InlineKeyboardButton(text='Большая игра', callback_data='game_big')],
        [InlineKeyboardButton(text='Очень большая игра', callback_data='game_mega')],
        [InlineKeyboardButton(text='Другие предложения', callback_data='game_other')]
    ])

buy_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='купить', url='http://ya.ru')],
        [InlineKeyboardButton(text='назад', callback_data='back_to_catalog')]   # нужно добавить хэндлер в main
    ]
)

# меню админское
admin_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='пользователи', callback_data='users')],     # тригеррит на users
        [InlineKeyboardButton(text='статистика', callback_data='stat')],
        [
            InlineKeyboardButton(text='блокировка', callback_data='block'),     # эти две клавиши в одной строке
            InlineKeyboardButton(text='разблокировка', callback_data='unblock')
        ]
        ]
)
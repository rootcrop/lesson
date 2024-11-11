from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

## Создайте и дополните клавиатуры:
##0 В главную (обычную) клавиатуру меню добавьте кнопку "Купить"
start_kb=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='О нас'), KeyboardButton(text='Стоимость')],
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
        [InlineKeyboardButton(text='Средняя игра', callback_data='medium')],
        [InlineKeyboardButton(text='Большая игра', callback_data='big')],
        [InlineKeyboardButton(text='Очень большая игра', callback_data='mega')],
        [InlineKeyboardButton(text='Другие предложения', callback_data='other')]
    ])

buy_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='купить', url='http://ya.ru')],
        [InlineKeyboardButton(text='назад', callback_data='back_to_catalog')]   # нужно добавить хэндлер в main
    ]
)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Уроки'),
            KeyboardButton(text="Тест"),
        ],

    ],

    resize_keyboard=True
)
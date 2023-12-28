from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тест по русскому"),
            KeyboardButton(text="Тест по английскому"),
        ],
        [
            KeyboardButton(text="Выход")
        ]
    ],
    resize_keyboard=True
)
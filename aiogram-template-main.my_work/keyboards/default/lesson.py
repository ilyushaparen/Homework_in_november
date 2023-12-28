from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
lesson = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Первый урок"),
            KeyboardButton(text="Второй урок"),
        ],
        [
            KeyboardButton(text="Третий урок"),
            KeyboardButton(text="Четвертый урок"),
        ],
        [
            KeyboardButton(text="Пятый урок"),

        ],
        [
            KeyboardButton(text="Выход"),
        ],
    ],
    resize_keyboard=True
)
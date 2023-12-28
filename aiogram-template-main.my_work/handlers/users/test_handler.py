from aiogram.types import Message
from loader import dp
from keyboards.default.butter import menu
from keyboards.default.Test import test

@dp.message_handler(text="Выход")
async def get(message: Message):
    await message.answer("Главная", reply_markup=test)


@dp.message_handler(text="Тест по русскому")
async def get(message: Message):
    await message.answer("https://onlinetestpad.com/ru/tests/russian")
@dp.message_handler(text="Тест по английскому")
async def get(message: Message):
    await message.answer("https://puzzle-english.com/level-test",)


from aiogram.types import Message
from loader import dp
from loader import dp
from keyboards.default.lesson import lesson
from keyboards.default.Test import test
from keyboards.default.butter import menu
from aiogram.types import Message


@dp.message_handler(text="Выход")
async def get(message: Message):
    await message.answer("Главня", reply_markup=menu)



@dp.message_handler(text="Первый урок")
async def get(message: Message):
    await message.answer("https://youtu.be/7_qg_KVByS0?si=zcQ9AdPwLkWsYaFD")

@dp.message_handler(text="Второй урок")
async def get(message: Message):
    await message.answer("https://youtu.be/Uh_-j8BS-NM?si=hFZmSaVHRT61Fl4z")

@dp.message_handler(text="Третий урок")
async def get(message: Message):
    await message.answer("https://youtu.be/dvLyDEA5aOg?si=Q1-YZwgO7EyFHxlV")

@dp.message_handler(text="Четвертый урок")
async def get(message: Message):
    await message.answer("https://youtu.be/eaCSJqY32l8?si=jgttESOdKlMzi-sC")

@dp.message_handler(text="Пятый урок")
async def get(message: Message):
    await message.answer("https://youtu.be/9Tq1yfWubYc?si=jjD748ynGQVvtNcN")
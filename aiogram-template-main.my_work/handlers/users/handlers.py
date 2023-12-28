from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.butter import menu
from loader import dp
from keyboards.default.lesson import lesson
from keyboards.default.Test import test
from aiogram.types import Message

@dp.message_handler(text='Уроки')
async def get(message: Message):
    await message.answer("Уроки",reply_markup=lesson)

@dp.message_handler(text="Тест")
async def get(message: Message):
    await message.answer("Тесты",reply_markup=test)

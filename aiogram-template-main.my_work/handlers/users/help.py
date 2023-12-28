from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.reply(f"Этот бот поможет вам научиться начальному анлгийскому \nСоздатель:https://t.me/Whoami7780")
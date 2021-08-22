from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard, ru_keyboard, en_keyboard, uz_keyboard_structure, ru_keyboard_structure, en_keyboard_structure
from loader import dp, bot


@dp.message_handler(Text(equals="🔝 Bosh menyu"))
async def back_all_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Toshkent kimyo-texnologiya instituti</b>",
        reply_markup=uz_keyboard
    )


@dp.message_handler(Text(equals="🔝 Главное меню"))
async def back_all_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Ташкентский химико-технологический институт</b>",
        reply_markup=ru_keyboard
    )


@dp.message_handler(Text(equals="🔝 Main menu"))
async def back_all_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Tashkent Chemical-Technological Institute</b>",
        reply_markup=en_keyboard
    )


@dp.message_handler(Text(equals="🔙 Orqaga"))
async def back_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Kerakli institut tuzilmasini tanlang:</b>",
        reply_markup=uz_keyboard_structure
    )


@dp.message_handler(Text(equals="🔙 Назад"))
async def back_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Выберите желаемую структуру заведения:</b>",
        reply_markup=ru_keyboard_structure
    )


@dp.message_handler(Text(equals="🔙 Back"))
async def back_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Select the desired institution structure:</b>",
        reply_markup=en_keyboard_structure
    )

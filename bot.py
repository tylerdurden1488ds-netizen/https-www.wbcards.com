import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎨 Создать карточку")],
        [KeyboardButton(text="✏️ Исправить карточку")],
        [KeyboardButton(text="📂 История")],
        [KeyboardButton(text="⭐ Шаблоны")],
        [KeyboardButton(text="⚙️ Настройки")]
    ],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "<b>👋 Добро пожаловать в WB AI Studio</b>\n\n"
        "Я помогу создавать профессиональные карточки товаров.\n\n"
        "Выберите действие ниже.",
        reply_markup=menu
    )


@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "Доступные возможности:\n\n"
        "🎨 Создание карточек\n"
        "✏️ Исправление карточек\n"
        "📂 История\n"
        "⭐ Шаблоны\n"
        "⚙️ Настройки"
    )


@dp.message()
async def messages(message: Message):
    text = message.text

    if text == "🎨 Создать карточку":
        await message.answer(
            "📷 Отправьте фотографию товара или напишите его описание."
        )

    elif text == "✏️ Исправить карточку":
        await message.answer(
            "Напишите, что нужно изменить.\n\n"
            "Например:\n"
            "• сделать фон белым\n"
            "• добавить золотой текст\n"
            "• увеличить цену"
        )

    elif text == "📂 История":
        await message.answer("История пока пуста.")

    elif text == "⭐ Шаблоны":
        await message.answer(
            "В следующей версии здесь будут 26 шаблонов."
        )

    elif text == "⚙️ Настройки":
        await message.answer(
            "Настройки будут добавлены позже."
        )

    else:
        await message.answer(
            "Пока эта функция ещё не реализована."
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

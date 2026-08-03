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
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    ),
)

dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎨 Создать карточку")],
        [KeyboardButton(text="✏️ Исправить карточку")],
        [KeyboardButton(text="📂 История")],
        [KeyboardButton(text="⭐ Шаблоны")],
        [KeyboardButton(text="⚙️ Настройки")],
    ],
    resize_keyboard=True,
)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "<b>WB AI Studio</b>\n\n"
        "Выберите действие:",
        reply_markup=menu,
    )


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "/start — меню\n"
        "/help — помощь"
    )


@dp.message()
async def handler(message: Message):

    text = message.text

    if text == "🎨 Создать карточку":
        await message.answer(
            "Пришлите фотографию товара."
        )

    elif text == "✏️ Исправить карточку":
        await message.answer(
            "Опишите, что изменить."
        )

    elif text == "📂 История":
        await message.answer(
            "История пока пустая."
        )

    elif text == "⭐ Шаблоны":
        await message.answer(
            "Скоро здесь будут 26 шаблонов."
        )

    elif text == "⚙️ Настройки":
        await message.answer(
            "Настройки скоро появятся."
        )

    else:
        await message.answer(
            "Используйте кнопки меню."
        )


async def main():
    logging.info("WB AI Studio started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

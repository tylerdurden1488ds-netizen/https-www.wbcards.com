from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

router = Router()

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


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "<b>🎨 WB AI Studio</b>\n\n"
        "Создание карточек Wildberries\n"
        "через Gemini + Nano Banana",
        reply_markup=menu,
    )


@router.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "Отправьте фотографию товара\n"
        "или нажмите «Создать карточку»."
    )

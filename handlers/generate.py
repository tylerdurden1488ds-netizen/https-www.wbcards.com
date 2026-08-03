from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import CreateCard

router = Router()


@router.message(lambda message: message.text == "🎨 Создать карточку")
async def create_card(message: Message, state: FSMContext):
    await state.set_state(CreateCard.waiting_photo)

    await message.answer(
        "📷 Отправьте фотографию товара.\n\n"
        "Можно также отправить несколько фотографий."
    )


@router.message(CreateCard.waiting_photo)
async def get_photo(message: Message, state: FSMContext):

    if not message.photo:
        await message.answer(
            "❌ Отправьте именно фотографию."
        )
        return

    await state.update_data(
        photo=message.photo[-1].file_id
    )

    await state.set_state(CreateCard.waiting_description)

    await message.answer(
        "📝 Теперь напишите название товара.\n\n"
        "Например:\n"
        "Кроссовки мужские"
    )


@router.message(CreateCard.waiting_description)
async def get_description(message: Message, state: FSMContext):

    await state.update_data(
        product=message.text
    )

    await state.set_state(CreateCard.waiting_background)

    await message.answer(
        "🎨 Какой фон нужен?\n\n"
        "Например:\n"
        "Белый\n"
        "Горы\n"
        "Студия\n"
        "Мрамор"
    )


@router.message(CreateCard.waiting_background)
async def get_background(message: Message, state: FSMContext):

    await state.update_data(
        background=message.text
    )

    await state.set_state(CreateCard.waiting_style)

    await message.answer(
        "✨ Напишите стиль.\n\n"
        "Например:\n"
        "Apple\n"
        "Premium\n"
        "Luxury\n"
        "Минимализм"
      )
    @router.message(CreateCard.waiting_style)
async def get_style(message: Message, state: FSMContext):

    await state.update_data(
        style=message.text
    )

    await state.set_state(CreateCard.waiting_text)

    await message.answer(
        "📝 Какой текст добавить на карточку?\n\n"
        "Например:\n"
        "НОВИНКА\n"
        "ПРЕМИУМ\n"
        "100% ХЛОПОК"
    )


@router.message(CreateCard.waiting_text)
async def get_text(message: Message, state: FSMContext):

    await state.update_data(
        text=message.text
    )

    await state.set_state(CreateCard.waiting_price)

    await message.answer(
        "💰 Введите цену.\n\n"
        "Например:\n1999 ₽"
    )


@router.message(CreateCard.waiting_price)
async def get_price(message: Message, state: FSMContext):

    await state.update_data(
        price=message.text
    )

    await state.set_state(CreateCard.waiting_old_price)

    await message.answer(
        "💸 Введите старую цену.\n\n"
        "Например:\n2999 ₽"
    )


@router.message(CreateCard.waiting_old_price)
async def get_old_price(message: Message, state: FSMContext):

    await state.update_data(
        old_price=message.text
    )

    await state.set_state(CreateCard.waiting_discount)

    await message.answer(
        "🏷 Введите скидку.\n\n"
        "Например:\n-33%"
    )


@router.message(CreateCard.waiting_discount)
async def get_discount(message: Message, state: FSMContext):

    await state.update_data(
        discount=message.text
    )

    data = await state.get_data()

    from services.ai_service import AIService

ai = AIService()

await message.answer("🤖 Генерирую профессиональный промпт...")

prompt = await ai.create_prompt(
    product=data["product"],
    background=data["background"],
    style=data["style"],
    text=data["text"],
    price=data["price"],
    old_price=data["old_price"],
    discount=message.text,
)

result = await ai.generate(prompt)

await message.answer(result)

await state.clear()
✅ Все данные получены.

📦 Товар:
{data['product']}

🎨 Фон:
{data['background']}

✨ Стиль:
{data['style']}

📝 Текст:
{data['text']}

💰 Цена:
{data['price']}

💸 Старая цена:
{data['old_price']}

🏷 Скидка:
{message.text}

Следующим этапом будет генерация через Gemini.
"""
    )

    await state.clear()

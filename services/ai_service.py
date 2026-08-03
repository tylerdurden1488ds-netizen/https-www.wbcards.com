from services.gemini import generate_text


class AIService:

    async def create_prompt(
        self,
        product,
        background,
        style,
        text,
        price,
        old_price,
        discount,
    ):
        prompt = f"""
Ты профессиональный дизайнер карточек Wildberries.

Создай максимально подробный промпт для генерации изображения.

Товар:
{product}

Фон:
{background}

Стиль:
{style}

Текст:
{text}

Цена:
{price}

Старая цена:
{old_price}

Скидка:
{discount}

Карточка должна выглядеть как топовая карточка Wildberries 2026.

Используй дорогой стиль.

Максимальный реализм.

Читаемый текст.

Премиальная композиция.

8K.

Высокая детализация.
"""

        return prompt

    async def generate(self, prompt):
        return generate_text(prompt)

BANNED_WORDS = [
    "лучший",
    "лучшая",
    "лучшее",
    "№1",
    "номер 1",
    "скидка",
    "акция",
    "гарантируем",
    "100% гарантия",
]


def check_banned(text: str):
    text = text.lower()

    found = []

    for word in BANNED_WORDS:
        if word in text:
            found.append(word)

    return found


def build_prompt(
    product: str,
    background: str,
    style: str,
    text: str,
    price: str,
    old_price: str,
    discount: str,
):
    prompt = f"""
Создай премиальную карточку товара Wildberries.

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

Требования:

• формат 3:4

• максимально дорогой коммерческий дизайн

• профессиональная рекламная фотография

• студийный свет

• высокий контраст

• читаемый текст

• современная типографика

• дорогой минимализм

• стеклянные элементы

• объёмные тени

• реалистичные материалы

• качество 8K

• без водяных знаков

• без артефактов

• без ошибок в тексте
"""

    return prompt

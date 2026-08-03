import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.generate import router as generate_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(generate_router)


async def main():
    logging.info("WB AI Studio started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

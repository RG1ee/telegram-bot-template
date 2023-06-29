import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage import memory

from tgbot.databases.database import DataBaseHelper
from tgbot.settings.config import load_config
from tgbot.settings.consts import DB_NAME
from tgbot.misc.register_all_services import register_all_services

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.basicConfig(
            level=logging.INFO,
        ),
    )
    logger.info("Бот запущен")
    conf = load_config()

    starage = memory.MemoryStorage()
    bot = Bot(token=conf.tg_bot.token, parse_mode="html")
    bot["config"] = conf

    dp = Dispatcher(
        bot=bot,
        storage=starage,
    )

    await register_all_services(dp)

    try:
        DataBaseHelper(DB_NAME).create_all_tables
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот остановил свою работу")

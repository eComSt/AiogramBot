import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import common, ordering


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Если не указать storage, то по умолчанию всё равно будет MemoryStorage
    # Но явное лучше неявного =]
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(token="5887799871:AAEKass2GpBSHVWUefXCRseiKHHzyBiY12s")

    dp.include_router(common.router)
    dp.include_router(ordering.router)
    # сюда импортируй собственный роутер

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
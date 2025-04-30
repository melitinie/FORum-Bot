import asyncio
import logging

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher

from handlers.deal_products import start_handler, applying_deal_handler
from handlers.other_services_of_bank import other_services_of_bank
from handlers.Safe import safe_choosing
from handlers.approved_deal import approved_deal_handler
from handlers.questions import questions

from DataBase import DataBase
from API import GET_deal_info_all

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


async def bot_main():
    bot = Bot(token="7941402050:AAHQWbIr6FxAlMNnmYTy0_QMd75jsjmFXsM",
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    await DataBase.DataBase_start()
    await DataBase.DataBase_add_baseinfo()
    dp.include_routers(start_handler.router, applying_deal_handler.router,
                       other_services_of_bank.router, safe_choosing.router, approved_deal_handler.router,
                       questions.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

async def main():
    await asyncio.gather(
        GET_deal_info_all.run_fastapi(),
        bot_main()  # Функция запуска бота (должна быть асинхронной)
    )

if __name__ == "__main__":
    asyncio.run(main())

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Здравствуйте! Это чат-бот канала «ФОРум». Здесь Вы можете записаться на сделку и изучить услуги банка. Напоминаем – нашу переписку видят только сотрудники банка и Вы.",
                        reply_markup=kb.main)

@router.message(F.text.lower() == "записаться на сделку")
async def book_deal(message: Message):
    await message.answer("Пожалуйста, выберите интересующую Вас категорию услуг:",
                        reply_markup=kb.deal_category)

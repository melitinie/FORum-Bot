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

@router.message(F.text.lower() == "посмотреть услуги банка")
async def view_services(message: Message):
    await message.answer("Какие услуги Вас интересуют?",
                         reply_markup=kb.other_services)

@router.message(F.text.lower() == "задать вопрос")
async def ask_question(message: Message):
    await message.answer("Задайте Ваш вопрос и консультант ответит на него в ближайшее время")
    #Не знаю как это реализовать. Может быть считать ID клиента и направить его в БД, а как консультант с ним свяжется это уже другая история

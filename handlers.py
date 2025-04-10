from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

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

@router.callback_query(F.data == "safe")
async def process_safe(callback_query: CallbackQuery):
    await callback_query.message.answer("Вы выбрали сейф. Выберите опцию:",
                        reply_markup=kb.safe_root)
    await callback_query.answer()

@router.callback_query(F.data == "letter_of_credit")
async def process_safe(callback_query: CallbackQuery):
    await callback_query.message.answer("Вы выбрали аккредитив. Выберите опцию:",
                        reply_markup=kb.accr_root)
    await callback_query.answer()

@router.callback_query(F.data == "safe_and_letter_of_credit")
async def process_safe(callback_query: CallbackQuery):
    await callback_query.message.answer('Вы выбрали услугу "Аккредитив + Сейф". Выберите опцию:',
                        reply_markup=kb.safe_and_accr)
    await callback_query.answer()

@router.message(F.text.lower() == "посмотреть услуги банка")
async def view_services(message: Message):
    await message.answer("Какие услуги Вас интересуют?",
                         reply_markup=kb.other_services)

@router.message(F.text.lower() == "задать вопрос")
async def ask_question(message: Message):
    await message.answer("Задайте Ваш вопрос и консультант ответит на него в ближайшее время")
    #Не знаю как это реализовать. Может быть считать ID клиента и направить его в БД, а как консультант с ним свяжется это уже другая история

from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from keyboards import keyboard_questions

router = Router()

@router.message(F.text == "❓ Задать вопрос")
async def question_start(message: types.Message):
    message_to_user = '⭕️Пожалуйста, выберите интересующую категорию 👇'

    await message.answer(message_to_user, reply_markup=keyboard_questions.keyboard_questions())


#Аренда переговорных комнат - проводите ли вы сделку в Фора-Банке?
@router.callback_query(F.data == 'questions_FAQ')
async def question_FAQ(callback: types.CallbackQuery):
    message_to_user = '⭕️Вы можете ознакомиться со списком часто задаваемых вопросов на нашем <a href="https://www.forabank.ru/bank-info/faq/">официальном сайте.</a>'
    await callback.message.answer(message_to_user)
from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from keyboards import keyboard_start
from keyboards import keyboard_others_services_of_bank

router = Router()

#Посмотреть услуги банка
# @router.message(F.text == "📖 Посмотреть услуги банка")
# async def services_message(message: types.Message):
#     message_to_user = 'Другие услуги банка:'
#     await message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())

#Другие услуги банка
@router.callback_query(F.data == 'deal_other_services_of_bank')
async def services_message(callback: types.CallbackQuery):
    message_to_user = '⭕️Фора-Банк предоставляет большой спектр услуг для бизнес- и частных клиентов.\n\nВыберите вариант ниже, чтобы узнать подробнее 👇'
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())

@router.message(F.text == '📖 Посмотреть услуги банка')
async def services_message1(message: types.Message):
    message_to_user = '⭕️Фора-Банк предоставляет большой спектр услуг для бизнес- и частных клиентов.\n\nВыберите вариант ниже, чтобы узнать подробнее 👇'
    await message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())


#Услуги, связанные с сделкой
@router.callback_query(F.data == 'services_deal')
async def services_deal(callback: types.CallbackQuery):
    message_to_user = '️⭕️Совместно с основной услугой, Вы можете воспользоваться дополнительными услугами по сделке!\n\n▫️Хранение ключа для сейфовой ячейки — 1 000 руб.\n▫️Проверка/пересчёт денежных средств — рубли - 0,1% (минимум 2 000 руб.)\n▫️Доверенность по форме банка — к сейфовой ячейке - 500 руб.\n▫️Электронная регистрация\n\nВыберите услугу для записи 👇'
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_deal_services())

#Прочее
@router.callback_query(F.data == 'services_other')
async def services_other(callback: types.CallbackQuery):
    message_to_user = ('⭕️Фора-Банк также предоставляет другие услуги.\n\n'
                       '📖 Подробнее — на <a href="https://www.forabank.ru/">нашем сайте</a>.\n\nВыберите вариант ниже, чтобы записаться на консультацию 👇')
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_rest())

#Консультация специалиста
@router.callback_query(F.data == 'specialist_consult')
async def consultation(callback: types.CallbackQuery):
    message_to_user = 'Запишитесь на консультацию со специалистом'
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_specialist_consultation())












from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types

from keyboards import keyboard_start


router = Router()

# @router.message(Command("start"))
# async def start_message(message: types.Message):
#     message_to_user = "Здравствуйте! Это чат-бот канала «ФОРум». Здесь Вы можете записаться на сделку и изучить услуги банка. Напоминаем – нашу переписку видят только сотрудники банка и Вы"
#     await message.answer(message_to_user, reply_markup=keyboard_start.keyboard_start())


# @router.callback_query(F.text == 'nazad')
# async def start_message(callback: types.CallbackQuery):
#     message_to_user = "Здравствуйте! Это чат-бот канала «ФОРум». Здесь Вы можете записаться на сделку и изучить услуги банка. Напоминаем – нашу переписку видят только сотрудники банка и Вы"
#     await callback.message.answer(message_to_user, reply_markup=keyboard_start.keyboard_start())

#Реализация через клавиатуру (кнопки внутри не инлайн)
@router.message(Command("start"))
async def start_message(message: types.Message):
     message_to_user = "Здравствуйте! Это чат-бот канала «ФОРум». Здесь Вы можете записаться на сделку и изучить услуги банка.\n\nНапоминаем – нашу переписку видят только сотрудники банка и Вы!"
     await message.answer(message_to_user, reply_markup=keyboard_start.keyboard_main())










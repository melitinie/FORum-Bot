from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                          InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Записаться на сделку')],
    [KeyboardButton(text='Посмотреть услуги банка'), KeyboardButton(text='Задать вопрос')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

deal_category = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сейф', callback_data='safe')],
    [InlineKeyboardButton(text='Аккредитив', callback_data='letter_of_credit')],
    [InlineKeyboardButton(text='Сейф + аккредитив', callback_data='safe_and_letter_of_credit')],
    [InlineKeyboardButton(text='Сделки с цепочками', callback_data='chain_deal')],
    [InlineKeyboardButton(text='Другие услуги банка', callback_data='other_services')],
    [InlineKeyboardButton(text='Электронная регистрация сделок с недвижимостью', callback_data='electronic_deal_registration')],
    [InlineKeyboardButton(text='Аренда переговорных комнат', callback_data='book_negotiations_room')],
    [InlineKeyboardButton(text='Отправить документы на сделку', callback_data='send_documents')]
])
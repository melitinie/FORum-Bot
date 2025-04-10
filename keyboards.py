from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                          InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Записаться на сделку')],
     [KeyboardButton(text='Посмотреть услуги банка'), KeyboardButton(text='Задать вопрос')]
], #root
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
]) #deals

safe_root = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Сейф.", callback_data = "safe_sizes")],
    [InlineKeyboardButton(text="Сейф + зеркальный сейф", callback_data = "safe_mirror")],
    [InlineKeyboardButton(text="Сейф + зеркальный сейф + бесплатный сейф для риэлтора", callback_data = "safe_mirror_r")],
    [InlineKeyboardButton(text="Сейф + бесплатный сейф для риэлтора", callback_data = "safe_free_r")],
])

accr_root = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Аккредитив до 1 млн. руб. - 500 руб.", callback_data = "accr_below_mln")],
    [InlineKeyboardButton(text="Аккредитив свыше 1 млн. руб. - бесплатно", callback_data = "accr_above_mln")],
])

safe_and_accr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="«Стандарт» - 2100", callback_data = "accr_standart")],
    [InlineKeyboardButton(text="«Универсал» - 2300", callback_data = "accr_universal")],
    [InlineKeyboardButton(text="«ВИП» - 2400", callback_data = "accr_standart")],
])

other_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Услуги, связанные со сделкой', callback_data='deal_services')],
    [InlineKeyboardButton(text='Прочее', callback_data='other_ones')]
]) #other_services



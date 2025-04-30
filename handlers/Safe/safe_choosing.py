from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from keyboards import keyboard_safe_choosing
from keyboards import keyboard_others_services_of_bank
router = Router()

#Cообщение с выбором категории
@router.callback_query(F.data == 'safe')
async def safe_category(callback: types.CallbackQuery):
    message_to_user = ("⭕️Если у вас возникла необходимость в безопасном хранении документов, денег, драгоценностей или других ценных и важных для вас предметов или вы нуждаетесь в передаче большой суммы денег в процессе заключения сделки с недвижимостью, воспользуйтесь для этих целей услугой по аренде банковских сейфов!\n\nСейфовые хранилища Фора-Банка оборудованы по последнему слову охранной техники и соответствуют всем современным мировым требованиям к хранилищам такого рода.\n\n"
    '📖 Подробнее — на <a href="https://www.forabank.ru/private/bankovskie-seyfy/">нашем сайте</a>.')
    await callback.message.answer(message_to_user, reply_markup=keyboard_safe_choosing.keyboard_safe_choosing(), parse_mode = "HTML")


#Размеры сейфов
@router.callback_query(F.data == 'ordinary_safe')
async def safe_size(callback: types.CallbackQuery):
    message_to_user = '⭕️Вы выбрали вариант "сейф"!\n\nХраните документы, драгоценности и важные активы с максимальной защитой в наших сейфовых ячейках:\n\n▫️Сейф "Стандарт" — 3 500 руб./мес\n▫️Сейф "️Универсал" — 4 000 руб./мес.\n▫️Сейф "ВИП" — 5000 руб./мес.\n\nПожалуйста, выберите тип сейфа 👇'
    await callback.message.answer(message_to_user, reply_markup=keyboard_safe_choosing.keyboard_safe_size())

#?основная услуга выбрана? (!!!Наверное нужно удалить!!! Он не задействуется)
@router.callback_query(F.data == 'safe_standart')
async def deal_safe(callback: types.CallbackQuery):
    message_to_user = "Основная услуга выбрана"
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())

#Сейф + зеркальный сейф
@router.callback_query(F.data == 'safe_mirror_safe')
async def safe_mirror_safe(callback: types.CallbackQuery):
    message_to_user = '⭕️Вы выбрали вариант "сейф + зеркальный сейф"!\n\n▫️Сейф "Универсал" — 4 000 руб./мес. + Сейф "Стандарт" — 3 500 руб./мес.\n▫️Сейф "Стандарт" — 3 500 руб./мес. + Сейф "Стандарт" — 3 500 руб./мес.\n▫️Сейф "ВИП" — 5 000 руб./мес. + Сейф "Стандарт" — 3 500 руб./мес.\n\nПожалуйста, выберите тип сейфов 👇'
    await callback.message.answer(message_to_user, reply_markup=keyboard_safe_choosing.keyboard_safe_safe_mirror_safe_size())

#?основная услуга выбрана?
@router.callback_query(F.data == 'safe_universal_standart')
async def deal_safe(callback: types.CallbackQuery):
    message_to_user = "Основная услуга выбрана"
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())

#Сейф + зеркальный сейф + бесплатный сейф для риелтора
@router.callback_query(F.data == 'safe_mirror_safe_free')
async def deal_safe(callback: types.CallbackQuery):
    message_to_user = '⭕️Вы выбрали вариант "сейф + зеркальный сейф + бесплатный сейф для риелтора"!\n\n▫️Сейф "Универсал" — 4 000 руб./мес. + Сейф "Стандарт" — 3 500 руб./мес. + бесплатный сейф для риелтора\n▫️Сейф "Универсал" — 4 000 руб./мес. + Сейф "Стандарт" — 3 500 руб./мес. + бесплатный сейф для риелтора\n▫️Сейф "ВИП" — 5 000 руб./мес. + Сейф "Стандарт" — 3 500 руб./мес. + бесплатный сейф для риелтора\n\nПожалуйста, выберите тип сейфов 👇'
    await callback.message.answer(message_to_user, reply_markup=keyboard_safe_choosing.keyboard_safe_mirror_free_for_reiltor())

#?основная услуга выбрана?
@router.callback_query(F.data == 'safe_universal_standart_free')
async def deal_safe(callback: types.CallbackQuery):
    message_to_user = "Основная услуга выбрана"
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())

#Сейф + бесплатный сейф для риелтора
@router.callback_query(F.data == 'safe_safe_free')
async def safe_mirror_safe_free(callback: types.CallbackQuery):
    message_to_user = '⭕️Вы выбрали вариант "сейф + бесплатный сейф для риелтора"!\n\n▫️Сейф "Стандарт" — 3 500 руб./мес. + бесплатный сейф для риелтора\n▫️Сейф "Универсал" — 4 000 руб./мес. + бесплатный сейф для риелтора\n▫️Сейф "ВИП" — 5 000 руб./мес. + бесплатный сейф для риелтора\n\nПожалуйста, выберите тип сейфов 👇'
    await callback.message.answer(message_to_user, reply_markup=keyboard_safe_choosing.keyboard_safe_safe_free())

#?основная услуга выбрана?
@router.callback_query(F.data == 'safe_standart_free')
async def deal_safe(callback: types.CallbackQuery):
    message_to_user = "Основная услуга выбрана"
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())






from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from keyboards import keyboard_start
from keyboards import keyboard_applying_for_deal
from keyboards import keyboard_deal_online_registation
from keyboards import keyboard_deal_with_chain
from keyboards import keyboard_deal_safe
from keyboards import keyboard_others_services_of_bank
from keyboards import keyboard_akkreditiv
router = Router()

# @router.callback_query(F.data == 'bank_deal')
# async def products_message(callback: types.CallbackQuery):
#     message_to_user = 'Выберете пожалуйста тип сделки:'
#     await callback.message.answer(message_to_user, reply_markup=keyboard_applying_for_deal.keyboard_category_of_deal())


@router.message(F.text == "📝 Записаться на сделку")
async def products_message(message: types.Message):
    message_to_user = '⭕️Фора-Банк – надежный партнер для ваших финансовых операций. Мы предлагаем полный спектр услуг для безопасных и комфортных сделок.\n\n📍Все услуги доступны в отделениях банка или онлайн – просто выберите нужный вариант, и мы подберем удобное время для консультации!\n\nВыберите тип сделки для записи 👇'
    keyboard_applying_for_deal.keyboard_category_of_deal()
    await message.answer(message_to_user, reply_markup=keyboard_applying_for_deal.keyboard_category_of_deal())


#Аренда переговорных комнат - проводите ли вы сделку в Фора-Банке?
@router.callback_query(F.data == 'deal_meeting_rooms_rent')
async def transaction_in_bank(callback: types.CallbackQuery):
    message_to_user = '⭕️При проведении сделки в ФОРА-Банке, аренда переговорной комнаты бесплатна!\n\nПроводите ли вы сделку в Фора-Банке? 👇'
    await callback.message.answer(message_to_user, reply_markup=keyboard_applying_for_deal.keyboard_deal_meeting_rooms_rent())

#Да
@router.callback_query(F.data == 'deal_meeting_room_rent_yes')
async def admitted(callback: types.CallbackQuery):
    await callback.message.answer(
        "При проведении сделки в ФОРА-Банке, аренда переговорной комнаты бесплатна. Напишите ваш номер телефона и мы перезвоним вам в течение 30 минут")

#Нет
@router.callback_query(F.data == 'deal_meeting_room_rent_no')
async def deny(callback: types.CallbackQuery):
    await callback.message.answer(
        '⭕️В Фора-Банке действуют следующие тарифы на аренду переговорной комнаты:\n\n▫️350 руб./полчаса\n▫️700 руб./час\n\nВы бы хотели провести переговоры в Фора-Банке? 👇', reply_markup=keyboard_applying_for_deal.keyboard_offline_transaction())

#Да записать на встр 350р 700р
@router.callback_query(F.data == 'offline_meeting_yes')
async def yes_350_r(callback: types.CallbackQuery):
    await callback.message.answer("Напишите ваш номер телефона и мы перезвоним в течение 30 минут")

#Нет не записать на встр 350р 700р
@router.callback_query(F.data == 'offline_meeting_no')
async def no_350_r(callback: types.CallbackQuery):
    await callback.message.answer("Тогда предлагаем ознакомиться с другими услугами нашего банка через меню ниже 👇", reply_markup=keyboard_start.keyboard_main())

#Электронная регистрация сделок с недвижимостью
@router.callback_query(F.data == 'deal_online_registation')
async def deal_online_registation(callback: types.CallbackQuery):
    message_to_user = ("⭕️Фора-Банк на основе партнёрства с РОСРЕЕСТРом приступил к оказанию услуг по электронной регистрации сделок с недвижимостью.\n\n🔥Подать документы на регистрацию сделки или же осуществить сделку с недвижимостью «под ключ», от подготовки документов до регистрации, стало намного удобнее. Теперь все, кто занят вопросом покупки/продажи недвижимости могут завершить процесс оформления, не тратя время на посещения государственных организаций!\n\n▫️1 продавец, 1 покупатель, 1 объект — 6 500 руб.\n▫️1 продавец, 1 покупатель, 1 объект + доп. продавец/покупатель —️ 6 500 руб. + 1500 руб.\n▫️1 продавец, 1 покупатель, 1 объект + доп. объект — 6 500 руб. + 4 000 руб.\n▫️Один из участников юр. лицо — 6 500 руб. + 2 000 руб.\n\n"
                       '📖Подробнее — на <a href="https://www.forabank.ru/elektr-registraciya/">нашем сайте</a>.\n\nСделайте Ваш выбор ниже 👇')
    await callback.message.answer(message_to_user, reply_markup=keyboard_deal_online_registation.category_of_deal_online_registation())

#Сделки с цепочками
@router.callback_query(F.data == 'deal_with_chain')
async def deal_with_chain(callback: types.CallbackQuery):
    message_to_user = "⭕️Выгодное пакетное предложение — арендуйте до 10 сейфов (20 арендаторов) за 6 500 рублей!\n\nСделайте Ваш выбор ниже 👇"
    await callback.message.answer(message_to_user, reply_markup=keyboard_deal_with_chain.keyboard_deal_with_chain())

#При расчетах используется акредитив свыше 1 млн. рублей
@router.callback_query(F.data == 'deal_safe')
async def deal_safe(callback: types.CallbackQuery):
    message_to_user = ('⭕️Вы выбрали вариант "сейф + аккредитив"! Вместе выгоднее!\n\n▫️Аккредитив + Сейф "Стандарт" — 2 100 руб.\n▫️Аккредитив + Сейф "Универсал" — 2 300 руб.\n▫️Аккредитив + Сейф "ВИП" — 2 400 руб.\n\n(При расчётах используется аккредитив свыше 1 миллиона рублей)\n\n'
    '📖Подробнее — на <a href="https://www.forabank.ru/private/bankovskie-seyfy/">нашем сайте</a>.\n\nСделайте Ваш выбор ниже 👇')
    await callback.message.answer(message_to_user, reply_markup=keyboard_deal_safe.keyboard_deal_safe())

#?основная услуга выбрана?
@router.callback_query(F.data == 'safe_plus_acreditiv')
async def deal_safe(callback: types.CallbackQuery):
    message_to_user = "Основная услуга выбрана"
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())

#АКРЕДИТИВ
@router.callback_query(F.data == 'deal_accreditive')
async def acreditiv(callback: types.CallbackQuery):
    message_to_user = ('⭕️Планируете покупку или продажу недвижимости? Позаботьтесь о безопасности сделки с аккредитивом от Фора-Банка!\n\nАккредитив — современная и безопасная форма расчетов при сделках с недвижимостью.\n\n🔥Выгодные условия: бесплатно — при сумме от 1 миллиона рублей и всего 500 рублей — для сделок до 1 миллиона!\n\n⭕️Наши преимущества:\n▫️6 филиалов по РФ\n▫️90 офисов, в которых можно оформить аккредитив\n▫️Услуги нотариуса и регистратора\n\n'
    '📖 Подробнее — на <a href="https://www.forabank.ru/private/akkreditivy/">нашем сайте</a>.\n\n'
    'Выберите аккредитив для записи на консультацию 👇')
    await callback.message.answer(message_to_user, reply_markup=keyboard_akkreditiv.keyboard_akkreditiv_size(), parse_mode = "HTML")

#?основная услуга выбрана?
@router.callback_query(F.data == 'akkreditiv')
async def deal_safe(callback: types.CallbackQuery):
    message_to_user = "Основная услуга выбрана"
    await callback.message.answer(message_to_user, reply_markup=keyboard_others_services_of_bank.keyboard_other_services())


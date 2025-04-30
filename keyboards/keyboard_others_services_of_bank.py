from aiogram.utils.keyboard import InlineKeyboardBuilder

#Раздел "другие услуги банка"
#от "как назвать?" - 2 кнопки услуги связанные со сделкой и прочее
def keyboard_other_services():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Услуги, связанные со сделкой", callback_data="services_deal")
    keyboard_builder.button(text="Прочие услуги", callback_data="services_other")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

#клавиатура от услуг связанных со сделкой
def keyboard_deal_services():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Хранение ключа для сейфовой ячейки", callback_data="approved_storage-key-for-safe-box")
    keyboard_builder.button(text="Проверка/пересчет денежных средств", callback_data="approved_cash-checking-counting")
    keyboard_builder.button(text="Доверенность по форме банка", callback_data="approved_trustee-safebox")
    keyboard_builder.button(text="Электронная регистрация", callback_data="deal_online_registation")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

#клавиатура от прочее
def keyboard_rest():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Индивидуальный сейф после сделки", callback_data="approved_individual-safe-after-deal")
    keyboard_builder.button(text="Вклад (услуга Абсолютная гаратния)", callback_data="approved_deposit-serivice-absolute-garantee")
    keyboard_builder.button(text="Открытие текущего счёта", callback_data="approved_openning-current-account")
    keyboard_builder.button(text="Карта с кешбэком", callback_data="approved_cashback-card")
    keyboard_builder.button(text="Обмен валюты", callback_data="approved_money-exchange")
    keyboard_builder.button(text="Монеты/золото", callback_data="approved_coins-or-gold")
    keyboard_builder.button(text="Юрист-онлайн", callback_data="approved_lawyer-online")
    keyboard_builder.button(text='Сертификат "проверка здоровья"', callback_data="approved_certificate-health-check")
    keyboard_builder.button(text='Сертификат "здоровый ребёнок"', callback_data="approved_certificate-healthy-child")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def keyboard_specialist_consultation():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Как записаться на сделку?", callback_data="I_don't_know")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


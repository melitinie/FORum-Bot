from aiogram.utils.keyboard import InlineKeyboardBuilder

#Сейф + аккредитив
def keyboard_deal_safe():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Аккредитив + Сейф "Стандарт"', callback_data='approved_safe+acred_standart')
    keyboard_builder.button(text='Аккредитив + Сейф "Универсал"', callback_data='approved_safe+acred_universal')
    keyboard_builder.button(text='Аккредитив + Сейф "ВИП"', callback_data='approved_safe+acred_VIP')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

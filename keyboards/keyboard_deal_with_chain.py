from aiogram.utils.keyboard import InlineKeyboardBuilder


def keyboard_deal_with_chain():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Консультация специалиста', callback_data='approved_specialist-consultation')
    keyboard_builder.button(text='Пакетное предложение: до 10 сейфов (20 арендаторов)', callback_data='approved_packagedeal-under10safes-20arenders')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

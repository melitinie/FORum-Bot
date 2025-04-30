from aiogram.utils.keyboard import InlineKeyboardBuilder


def category_of_deal_online_registation():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='1 продавец, 1 покупатель, 1 объект', callback_data='approved_onlinereg-seller1-buyer1-object')
    keyboard_builder.button(text='1 продавец, 1 покупатель, 1 объект + доп. продавец/покупатель', callback_data='approved_onlinereg-1seller-1buyer-object-extra-seller-or-buyer')
    keyboard_builder.button(text='1 продавец, 1 покупатель, 1 объект + доп. объект', callback_data='approved_onlinereg-1seller-1buyer-1object-1extra-object')
    keyboard_builder.button(text='Один из участников юр. лицо', callback_data='approved_onlinereg-1seller-1buyer-urface')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()



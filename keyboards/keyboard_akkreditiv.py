from aiogram.utils.keyboard import InlineKeyboardBuilder

def keyboard_akkreditiv_size():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Аккредитив до 1 млн. руб.', callback_data='approved_akkreditiv-under-1mill')
    keyboard_builder.button(text='Аккредитив свыше 1 млн. руб.', callback_data='approved_akkreditiv-ahead-1mill-for-free')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
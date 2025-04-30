from aiogram.utils.keyboard import InlineKeyboardBuilder

#Выбор категории сейфа
def keyboard_safe_choosing():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Сейф', callback_data='ordinary_safe')
    keyboard_builder.button(text='Сейф + зеркальный сейф', callback_data='safe_mirror_safe')
    keyboard_builder.button(text='Сейф + зеркальный сейф + бесплатный сейф для риэлтора', callback_data='safe_mirror_safe_free')
    keyboard_builder.button(text='Сейф + бесплатный сейф для риэлтора', callback_data='safe_safe_free')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

#Размеры сейфов
def keyboard_safe_size():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Сейф "Cтандарт"', callback_data='approved_safe-standart')
    keyboard_builder.button(text='Сейф "Универсал"', callback_data='approved_safe-universal')
    keyboard_builder.button(text='Сейф "ВИП"', callback_data='approved_safe-VIP')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

#Сейф + зеркальный сейф
def keyboard_safe_safe_mirror_safe_size():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Сейф "Универсал" + Сейф "Cтандарт"', callback_data='approved_safe-universal-and-standart')
    keyboard_builder.button(text='Сейф "Cтандарт" + Сейф "Cтандарт"', callback_data='approved_safe-standart-and-standart')
    keyboard_builder.button(text='Сейф "ВИП" + Сейф "Cтандарт"', callback_data='approved_safe-VIP-and-standart')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

#Сейф + зеркальный сейф + бесплатный сейф для риелтора
def keyboard_safe_mirror_free_for_reiltor():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Сейф "Универсал" + Сейф "Cтандарт" + бесплатный сейф для риелтора', callback_data='approved_safe-universal-and-standart-and-free-safe-for-ragent')
    keyboard_builder.button(text='Сейф "Cтандарт" + Сейф "Cтандарт" + бесплатный сейф для риелтора', callback_data='approved_safe-standart-and-standart-and-free-safe-for-ragent')
    keyboard_builder.button(text='Сейф "ВИП" + Сейф "Cтандарт" + бесплатный сейф для риелтора', callback_data='approved_safe-VIP-and-standart-and-free-safe-for-ragent')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

#Сейф + бесплатный сейф для риелтора
def keyboard_safe_safe_free():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Сейф "Cтандарт"', callback_data='approved_safe-standart-and-free-safe-for-ragent')
    keyboard_builder.button(text='Сейф "Универсал"', callback_data='approved_safe-universal-and-free-safe-for-ragent')
    keyboard_builder.button(text='Сейф "ВИП"', callback_data='approved_safe_VIP-and-free-safe-for-ragent')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()



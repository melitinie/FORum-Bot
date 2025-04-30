from aiogram.utils.keyboard import InlineKeyboardBuilder

def request_contact():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Отправить контакт", request_contact=True)
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()



def approved_deal_final():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Подтвердить запись", callback_data="final_deal_approved")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

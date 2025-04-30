from aiogram.utils.keyboard import InlineKeyboardBuilder


def keyboard_category_of_deal():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Сейф', callback_data='safe', width = 10)
    keyboard_builder.button(text='Аккредитив', callback_data='deal_accreditive', width = 10)
    keyboard_builder.button(text='Сейф + Аккредитив', callback_data='deal_safe')
    keyboard_builder.button(text='Сделки с цепочками', callback_data='deal_with_chain')
    keyboard_builder.button(text='Другие услуги банка', callback_data='deal_other_services_of_bank')
    keyboard_builder.button(text='Электронная регистрация сделок с недвижимостью', callback_data='deal_online_registation', width = 10)
    keyboard_builder.button(text='Аренда переговорных комнат', callback_data='deal_meeting_rooms_rent')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

#Аренда переговорных комнат
def keyboard_deal_meeting_rooms_rent():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Да', callback_data='approved_deal-meeting-room-rent-yes')
    keyboard_builder.button(text='Нет', callback_data='deal_meeting_room_rent_no')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()

def keyboard_offline_transaction():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Да', callback_data='approved_offline-meeting-yes')
    keyboard_builder.button(text='Нет', callback_data='offline_meeting_no')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()



from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def keyboard_start():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Записаться на сделку", callback_data="bank_deal")
    keyboard_builder.button(text="Посмотреть услуги банка", callback_data="bank_services")
    #keyboard_builder.button(text="Задать вопрос", callback_data="bank_questions")
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()

#это обычное меню с пуговкой
def keyboard_main():
    kb_list = [
        [KeyboardButton(text="📝 Записаться на сделку"), KeyboardButton(text="📖 Посмотреть услуги банка")],
        [KeyboardButton(text="❓ Задать вопрос")]]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    return keyboard
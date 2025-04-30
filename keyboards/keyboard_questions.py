from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def keyboard_questions():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Часто задаваемые вопросы", callback_data="questions_FAQ")
    keyboard_builder.button(text="Задать вопрос консультанту", callback_data="approved_questions-consultant")
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
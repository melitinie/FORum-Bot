import logging

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

import app.keyboards as kb
from app.menu import MenuTree

router = Router()
log = logging.getLogger(__name__)
menu_tree = MenuTree()


def create_menu_message(*, header: str = "", current_menu_id: int):
    menu_rows = menu_tree.get_menu(current_menu_id)
    menu_text = "\n".join([f"{i}. {item['title']}" for i, item in enumerate(menu_rows, 1)])
    builder = InlineKeyboardBuilder()
    builder.max_width = 4
    builder.row(
        *[InlineKeyboardButton(text=f"{i}. {row['title']}", callback_data=f"menu_id:{row['id']}")
          for i, row in enumerate(menu_rows, 1)]
    )
    if current_menu_id > 0:
        builder.row(
            InlineKeyboardButton(
                text="Назад",
                callback_data=f"menu_id:{menu_tree.find_row(current_menu_id)['parent_id']}",
            )
        )
    header_text = f"{header}\n\n" if header else ""
    return f"{header_text}{menu_text}", builder.as_markup()


@router.callback_query(lambda c: c.data and c.data.startswith("menu_id:"))
async def menu_handler(callback_query: CallbackQuery, state: FSMContext):
    log.debug(f'Received menu callback, data="{callback_query.data}"')
    menu_id = int(callback_query.data.split(":")[1])
    await state.update_data({"current_menu_id": menu_id})
    await callback_query.message.delete()
    row = menu_tree.find_row(menu_id)
    log.debug(f'Current menu row="{row}"')
    text, reply_markup = create_menu_message(
        header=f'"{row["title"]}", выберите категорию:' if row else "Выберите действие:",
        current_menu_id=row["id"] if row else 0,
    )
    await callback_query.message.answer(text, reply_markup=reply_markup)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    log.debug('Received "start" command')
    current_menu_id = 0 #(await state.get_data()).get("current_menu_id", 0)
    await message.answer(
        "Здравствуйте! Это чат-бот канала «ФОРум». Здесь Вы можете записаться на сделку и изучить услуги банка. Напоминаем – нашу переписку видят только сотрудники банка и Вы.")
    text, reply_markup = create_menu_message(
        header="Выберите действие:", current_menu_id=current_menu_id
    )
    await message.answer(text, reply_markup=reply_markup)

    # await message.answer("Здравствуйте! Это чат-бот канала «ФОРум». Здесь Вы можете записаться на сделку и изучить услуги банка. Напоминаем – нашу переписку видят только сотрудники банка и Вы.",
    #                     reply_markup=kb.main)

# @router.message(F.text.lower() == "записаться на сделку")
# async def book_deal(message: Message):
#     await message.answer("Пожалуйста, выберите интересующую Вас категорию услуг:",
#                         reply_markup=kb.deal_category)
#
# @router.message(F.text.lower() == "посмотреть услуги банка")
# async def view_services(message: Message):
#     await message.answer("Какие услуги Вас интересуют?",
#                          reply_markup=kb.other_services)
#
# @router.message(F.text.lower() == "задать вопрос")
# async def ask_question(message: Message):
#     await message.answer("Задайте Ваш вопрос и консультант ответит на него в ближайшее время")
#     #Не знаю как это реализовать. Может быть считать ID клиента и направить его в БД, а как консультант с ним свяжется это уже другая история

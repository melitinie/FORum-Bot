from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Здравствуйте! Это чат-бот канала «ФОРум». Здесь Вы можете записаться на сделку и изучить услуги банка. Напоминаем – нашу переписку видят только сотрудники банка и Вы.")

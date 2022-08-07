from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    await message.reply(f"Hello, mr. {message.from_user.full_name}!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["astart"], state="*", is_admin=True)

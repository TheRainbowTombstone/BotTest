from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove

from tgbot.keyboards.reply import pour


async def user_start(message: Message):
    await message.answer(f"Вечер в хату, {message.from_user.full_name}!\nХочешь выпить, а не с кем?")
    await message.answer(f"Наливай!!!", reply_markup=pour)

async def user_cont(message: Message):
    await message.answer("О, снова ты! Ну, располагайся, наливай.", reply_markup=pour)

async def pour_alko(message: Message):
    if message.text == "Налить спирт":
        await message.answer("О, смотрю, градуса не боишься! Твоё здоровье!", reply_markup=ReplyKeyboardRemove())
    elif message.text == "Налить водочки":
        await message.answer("Льёшь как девочка, давай до краёв! Будем!", reply_markup=ReplyKeyboardRemove())
    elif message.text == "Налить пивчанского":
        await message.answer("Самое время разогнаться, господин Торетто. Cheerse.", reply_markup=ReplyKeyboardRemove())
    elif message.text == "Сам налей!":
        await message.answer("Если хочешь продолжения беседы, наливай.")



def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

def user_continue(dp: Dispatcher):
    dp.register_message_handler(user_cont, commands=["continue"], state="*")


def pour_alkohol(dp: Dispatcher):
    dp.register_message_handler(pour_alko)

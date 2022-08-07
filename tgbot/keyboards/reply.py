from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

pour = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Налить спирт"),
            KeyboardButton(text="Налить водочки")
        ],
        [
            KeyboardButton(text="Налить пивчанского"),
            KeyboardButton(text="Сам налей!")
        ],

    ],
    resize_keyboard=True
)


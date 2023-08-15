from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

BOT_TOKEN = "6593693542:AAHZNVVPju5nesUbB6HnL0RJoflI-HKx5qM"

bot = Bot(BOT_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    # print(message)
    text = f"Hi {message.from_user.first_name} ! Welcome to My bots"
    await message.answer(text)


@dp.message_handler(commands='inline_buttons')
async def inline_button(message: types.Message):
    design = [
        [InlineKeyboardButton("Button 1", callback_data='btn1'),
         InlineKeyboardButton("My account", url='https://t.me/foziljonn_04')],
        [InlineKeyboardButton("Button 3", callback_data='btn3')],
        [InlineKeyboardButton("Instagram", web_app=WebAppInfo(url="https://instagram.com"))]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await message.answer("Choose one", reply_markup=ikm)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

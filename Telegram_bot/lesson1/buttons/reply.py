from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "6593693542:AAHZNVVPju5nesUbB6HnL0RJoflI-HKx5qM"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    # print(message)
    text = f"Hi {message.from_user.first_name} ! Welcome to My bots"
    await message.answer(text)


@dp.message_handler(commands='reply_button')
async def start_handler(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Button 1", "Button 2")
    markup.add("Button 3", "Button 4")
    # markup.add("Button 3")
    markup.add("Button 4")

    design = [
        ["Button 1", KeyboardButton("☎️ Phone number", request_contact=True),
         KeyboardButton("Send location 📍 ", request_location=True)],
        ["Button 4", "Button 5", "Button 6"],
        ["Button 7", "Button 8", "Button 9"],

    ]
    markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

    await message.answer("Reply button show", reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

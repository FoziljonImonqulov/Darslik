from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
import logging

Bot_Token = "6657313336:AAFDc1-6r59unMTv3rwI7VB__uH3cK-LqO8"
bot = Bot(Bot_Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start_(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Filiallar📍"), KeyboardButton('Start train🏋'))
    markup.add(KeyboardButton("Admin☎"), KeyboardButton('Nearest location📍', request_location=True))
    await message.answer("FitnessHall ga xush kelibsiz", reply_markup=markup)


@dp.message_handler(Text("Admin☎"))
async def admin_(message: types.Message):
    await message.bot.send_contact(message.from_user.id, "+998931174113", "Foziljon", "Imonqulov")


# @dp.message_handler(Text("Filiallar📍"))
# async def send_branch(message: types.Message):
#     await message.bot.send_location(message.from_user.id, )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

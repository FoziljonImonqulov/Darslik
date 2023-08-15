import markdown
from aiogram import Dispatcher, types, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

BOT_TOKEN = "6651525694:AAGxPOfgDQ8QkHphOocqD7qHwYaCJXBk7S8"

bot = Bot(BOT_TOKEN)

dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['register'])
async def register_handler(message: types.Message, state: FSMContext):
    await state.set_state("fullname")
    await message.answer("Fullname : ")


@dp.message_handler(state='fullname')
async def fullname_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text
    await state.set_state('phone')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("☎ phone number", request_contact=True))
    await message.answer("Send your number: ",reply_markup=markup)


@dp.message_handler(content_types=types.ContentType.CONTACT, state='phone')
async def phone_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.contact.phone_number
    text = f"Fullname: {data.get('fullname')}" \
           f"phone number: {data.get('phone')}"
    await message.answer(text)
    await state.finish()
    await message.answer("Siz ro'yxatdan o'tdingiz! ", reply_markup=ReplyKeyboardRemove)


# @dp.message_handler(commands=['start'])
# async def start_(message: types.Message):
#     text1 = f"Hi *{message.from_user.first_name}* welcome to my bot"
#     text = f"||Salom||"
#     await message.answer(text, parse_mode="MarkdownV2")
#
#
# @dp.message_handler(commands=['lang', 'language'])
# async def language_(message: types.Message):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton('eng🇺🇲'), KeyboardButton('uzb🇺🇿'))
#     await message.answer("Choose language", reply_markup=markup)
#
#
# @dp.message_handler(lambda msg: msg.text in ("eng🇺🇲", "uzb🇺🇿"))
# async def choose_language(message: types.Message):
#     if message.text == "uzb🇺🇿":
#         await message.answer("Assalomu Alaykum!")
#     else:
#         await message.answer("Hello!")
#
# @dp.message_handler(CommandStart())
# async def rental_link(messge:types.Message):
#     print(messge)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

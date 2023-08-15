import logging
import os

print(os.getcwd())
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Filter, CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram_bot.fastfood.sql1 import Tbot

BOT_TOKEN = '6651525694:AAGxPOfgDQ8QkHphOocqD7qHwYaCJXBk7S8'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logger = logging.getLogger(__name__)


class Register(StatesGroup):
    fullname = State()
    phone_number = State()
    language = State()
    first_name = State()
    city = State()
    lang = State()


class inside_o(StatesGroup):
    first_name = State()
    city = State()
    lang = State()


@dp.message_handler(commands="start")
async def register_handler(message: types.Message):
    a = message['from']['id']
    data = {
        "user_id": message["from"]['id'],
        'is_bot': message['from']['is_bot'],
        "first_name": message['from']['first_name'],
        'last_name': message['from']['last_name'],
        'username': message['from']['username'],
        'language_code': message['from']['language_code']
    }
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Telefon raqamingizni yuboring", request_contact=True))
    obj = Tbot(**data)
    if not obj.check_is_available():
        obj.insert_data()
    await message.answer('Iltimos royxatdan o\'ting', reply_markup=markup)


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def fullname_handler(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    await Register.first_name.set()
    async with state.proxy() as data:
        data["phone_number"] = contact
    await message.answer("Ismingizni yozib yuboring: ")


@dp.message_handler(state=Register.first_name)
async def contact_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["first_name"] = message.text
    data = await state.get_data()
    await message.answer(f"{data.get('first_name')} {data.get('phone_number')}")
    obj = Tbot(**data)
    if obj:
        obj.update_data()
    design = [
        [InlineKeyboardButton("Ha", callback_data='ha'), InlineKeyboardButton("yo'q", callback_data='yoq')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await message.answer("Malumot to'g'rimi", reply_markup=ikm)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data in ('ha', 'yoq'))
async def main_menu(callback: types.CallbackQuery):
    if callback.data == 'ha':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("🍽 Menu"))
        markup.add(KeyboardButton("🛒 Buyrtmalar tarixi"), KeyboardButton("✍  Fikr bildirish"))
        markup.add(KeyboardButton(" 🗒 Ma'lumot"), KeyboardButton("📞 Biz bilan aloqa"))
        markup.add(KeyboardButton("⚙️ Sozlamalar"))
        await callback.message.answer("Main menu ", reply_markup=markup)
    else:
        await register_handler(callback.message)


@dp.message_handler(lambda msg: msg.text in ("🍽 Menu"))
async def menu_(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(" 🚙 yetkazib berish "), KeyboardButton(" 🚲 Olib ketish"))
    markup.add(KeyboardButton("⬅Ortga"))
    await message.answer("O'zingizga qulay usluni tanlang: ", reply_markup=markup)


@dp.message_handler(lambda msg: msg.text.startswith("⬅Ortga"))
async def back(message: types.Message):
    await main_menu(message)


async def main_menu(reply_message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("🍽 Menu"))
    markup.add(KeyboardButton("🛒 Buyrtmalar tarixi"), KeyboardButton("✍  Fikr bildirish"))
    markup.add(KeyboardButton(" 🗒 Ma'lumot"), KeyboardButton("📞 Biz bilan aloqa"))
    markup.add(KeyboardButton("⚙️ Sozlamalar"))
    await reply_message.answer("Main menu ", reply_markup=markup)


@dp.message_handler(lambda msg: msg.text in (" 🚲 Olib ketish"))
async def by_me(message: types.Message):
    await message.answer("Tez orada...")


@dp.message_handler(lambda msg: msg.text in ("🚙 yetkazib berish "))
async def by_me(message: types.Message):
    await message.answer("Tez orada...")


@dp.message_handler(lambda msg: msg.text in ("🛒 Buyrtmalar tarixi"))
async def orders_history(message: types.Message):
    await message.answer("Siz hali buyurtma bermadingiz uni to'ldirish kerak ")


@dp.message_handler(lambda msg: msg.text in ("✍  Fikr bildirish"))
async def orders_history(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Hammasi yoqdi")
    markup.add("Yaxshi ⭐ ⭐ ⭐ ⭐")
    markup.add("Yoqmadi ⭐ ⭐ ⭐")
    markup.add("Yomon ⭐ ⭐ ")
    markup.add("Juda yomon 👎")
    markup.add("⬅Ortga")
    await message.answer("Fikringizni belgilang:", reply_markup=markup)


@dp.message_handler(
    lambda msg: msg in ("Hammasi yoqdi", "Yaxshi ⭐ ⭐ ⭐ ⭐", "Yoqmadi ⭐ ⭐ ⭐", "Yomon ⭐ ⭐ ", "Juda yomon 👎"))
async def get_sms(message: types.Message):
    chat_id = 1526992254
    if message.text == "Hammasi yoqdi":
        response = "Hammasi yoqdi"
        await message.bot.send_message(chat_id, response)
    elif message.text == "Yaxshi ⭐ ⭐ ⭐ ⭐":
        response = "Yaxshi ⭐ ⭐ ⭐ ⭐"  # Corrected the variable name
        await message.bot.send_message(chat_id, response)
    elif message.text == "Yoqmadi ⭐ ⭐ ⭐":
        response = "Yoqmadi ⭐ ⭐ ⭐"
        await message.bot.send_message(chat_id, response)
    elif message.text == "Yomon ⭐ ⭐ ":
        response = "Yomon ⭐ ⭐ "
        await message.bot.send_message(chat_id, response)
    else:
        response = "Juda yomon 👎"
        await message.bot.send_message(chat_id, response)


@dp.message_handler(lambda msg: msg.text in ("⬅Ortga"))
async def back(message: types.Message):
    await main_menu(message)


@dp.message_handler(lambda msg: msg.text in ("📞 Biz bilan aloqa"))
async def aloqa(message: types.Message):
    await message.bot.send_contact(message.chat.id, "+99893iin4113", "Imonqulov", "Foziljon")


@dp.message_handler(lambda msg: msg.text in ("🗒 Ma'lumot"))
async def info(message: types.Message):
    await message.answer("Bu yerda sizning kompanyangiz malumoti bolishi mumkun edi ")


@dp.message_handler(lambda msg: msg.text in ("⚙️ Sozlamalar"))
async def settings(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Ismni o'zgartishish"), KeyboardButton("Raqamni o'zgartirish"))
    markup.add(KeyboardButton("Shaharni O'zgartirish"), KeyboardButton("Tilni o'zgartirish"))
    markup.add(KeyboardButton("⬅Ortga"))
    await message.answer("Harakatni tanlang:", reply_markup=markup)


@dp.message_handler(lambda msg: msg.text in ("Ismni o'zgartishish"))
async def change_name(message: types.Message, state: FSMContext):
    await inside_o.first_name.set()
    await message.answer("Tez orada")


# @dp.message_handler(state=inside_o.first_name)
# async def changed_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['first_name'] = message.text
#     a = {'user_id': message.from_user.id}
#     data.update(a)
#     await state.finish()
#     obj = Tbot(**data)
#     obj.update_name()
#     await message.answer(f"Ismingiz {data['first_name']} ga o'zgarid ")


@dp.message_handler(lambda msg: msg.text in ("⬅Ortga"))
async def back(message: types.Message):
    await main_menu(message)


@dp.message_handler(commands='salom')
async def send_(message: types.Message):
    await message.bot.send_message(1526992254, "Salom")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

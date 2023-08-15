from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Filter, CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = '6593693542:AAHZNVVPju5nesUbB6HnL0RJoflI-HKx5qM'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Register(StatesGroup):
    fullname = State()
    phone_number = State()
    language = State()


@dp.message_handler(commands="start")
async def register_handler(message: types.Message):
    await Register.fullname.set()
    await message.answer("To'liq ism familya : ")


@dp.message_handler(state=Register.fullname)
async def fullname_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["fullname"] = message.text
    await Register.phone_number.set()
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("☎️phone number", request_contact=True))
    await message.answer("Telefon raqamingizni yuboring : ", reply_markup=markup)


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=Register.phone_number)
async def contact_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone_number"] = message.contact.phone_number
    data = await state.get_data()
    await message.answer(f"{data.get('fullname')} {data.get('phone_number')}")
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
        await register_handler()


@dp.message_handler(lambda msg: msg.text in ("🍽 Menu"))
async def menu_(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(" 🚙 yetkazib berish "), KeyboardButton(" 🚲 Olib ketish"))
    markup.add(KeyboardButton("Ortga ⬅"))
    await message.answer("O'zingizga qulay usluni tanlang: ", reply_markup=markup)


@dp.message_handler(lambda msg: msg.text in ("Ortga ⬅"))
async def back(message: types.Message):
    await main_menu()


@dp.message_handler(lambda msg: msg.text in (" 🚲 Olib ketish"))
async def by_me(message: types.Message):
    await message.answer("Tez orada...")


@dp.message_handler(lambda msg: msg.text in (" 🚙 yetkazib berish "))
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
    markup.add("⬅ortga")
    await message.answer("Siz hali buyurtma bermadingiz ", reply_markup=markup)


@dp.message_handler(lambda msg: msg.text in ("⬅ortga"))
async def back(message: types.Message):
    await main_menu()


@dp.message_handler(lambda msg: msg.text in ("📞 Biz bilan aloqa"))
async def aloqa(message: types.Message):
    await message.bot.send_contact("Bizning admin", "+99893iin4113", "Imonqulov Foziljon")


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


@dp.message_handler(lambda msg: msg.text in ("⬅Ortga"))
async def back(message: types.Message):
    await main_menu()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

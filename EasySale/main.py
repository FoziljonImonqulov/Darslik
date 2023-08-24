from aiogram import types, executor, Bot, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from EasySale.base import DB

BOT_TOKEN = "6415492254:AAGPJ2zP-3ciAG3cychLkN_jRHO_mVLKuo8"

bot = Bot(BOT_TOKEN)

dp = Dispatcher(bot, storage=MemoryStorage())

picture = []


class Item(StatesGroup):
    name = State()
    cost = State()
    description = State()
    number = State()
    picture = State()


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    if not DB().check_is_available(user_id=message.from_user.id):
        DB().insert_data(user_id=message.from_user.id, is_bot=message.from_user.is_bot,
                         first_name=message.from_user.first_name, last_name=message.from_user.last_name,
                         username=message.from_user.username, language_code=message.from_user.language_code)

    await message.answer(f"Assalomu alaykum {message.from_user.first_name} EasySale ga xushkelibsiz!\nWelcome! ")
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    markup.add(KeyboardButton("uzb"), KeyboardButton('eng'))
    await message.answer('Choose your languge\nTilni tanlang', reply_markup=markup)


@dp.message_handler(lambda msg: msg.text in ("uzb"))
async def language_(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Raqamingizni yuboring", request_contact=True))
    await message.answer("Iltimos botdan foydalanish uchun ro'yxtadan o'ting ", reply_markup=markup)


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler(message: types.Message):
    contac = message.contact.phone_number
    DB().update_data(phone_number=contac, user_id=message.from_user.id)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Sotib olaman"), KeyboardButton("Sotaman"))
    await message.answer("Quydagi tugamni tanlang!", reply_markup=markup)


@dp.message_handler(Text("Sotib olaman"))
async def bought_(message: types.Message):
    await message.bot.send_message(message.from_user.id, 'https://t.me/easy_sale_shop')


@dp.message_handler(Text("Sotaman"))
async def sale_(message: types.Message):
    await message.answer("Mahsulot rasmini yuboring")


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_(message: types.Message):
    await Item.name.set()
    await message.answer('Mahsulot nomini yozing\nmasalan Samsung A5')
    photo = message['photo'][-1]['file_id']
    picture.append(photo)


@dp.message_handler(state=Item.name)
async def name_(message: types.Message, state: FSMContext):
    await Item.cost.set()
    async with state.proxy() as data:
        data["name"] = message.text
    await message.answer('Qanchaga sotmoqchisiz narxini kiriting\n'
                         'masalan $400 ')


@dp.message_handler(state=Item.cost)
async def cost_(message: types.Message, state: FSMContext):
    await Item.number.set()
    async with state.proxy() as data:
        data['cost'] = message.text
    await message.answer('Telefon raqamingizni yuboring\n'
                         '+998931234567 < shaklda ')


@dp.message_handler(state=Item.number)
async def cost_(message: types.Message, state: FSMContext):
    await Item.description.set()
    async with state.proxy() as data:
        data['number'] = message.text
    await message.answer("mahsulotga umumiy tarif bering")


@dp.message_handler(state=Item.description)
async def desc_(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    data = await state.get_data()
    await state.finish()
    edited = f"""
Mahsulot turi:    {data['name']}
Mahsulot narxi 💲   {data['cost']}
Mahsulot holati :    {data['description']}
Foydalanuvchi raqami 📱   {data['number']}
[Bog'lanish uchun](message.from_user.username)
    """
    await message.bot.send_photo(-1001909378622, photo=picture[0], caption=edited, parse_mode='Markdown')
    picture.clear()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

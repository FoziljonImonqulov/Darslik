from aiogram import Dispatcher, types, Bot, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from sql1 import Users

BOT_TOKEN = "6651525694:AAGxPOfgDQ8QkHphOocqD7qHwYaCJXBk7S8"

bot = Bot(BOT_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_(message: types.Message):
    d = {
        "user_id": message["from"]['id'],
        'is_bot': message['from']['is_bot'],
        "first_name": message['from']['first_name'],
        'last_name': message['from']['last_name'],
        'username': message['from']['username'],
        'language_code': message['from']['language_code']
    }
    if not Users().check_user():
        Users(**d).insert_into()
    ln = ReplyKeyboardMarkup(resize_keyboard=True)
    l1 = KeyboardButton('/eng')
    l2 = KeyboardButton('/rus')
    ln.add(l1, l2)
    await message.answer('Tilni tanlang', reply_markup=ln)


@dp.message_handler(commands=['eng', 'rus'])
async def register(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Share my phone number 📱 ", request_contact=True)
    kb.add(btn1)
    text = f"Iltimos, ro'yxatdan o'ting"
    await message.answer(text, reply_markup=kb)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def menu_(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('/Menu'))
    markup.add(KeyboardButton('/Buyurtmalarim'))
    markup.add(KeyboardButton('/Admin'), KeyboardButton("/Sozlamalar"))

    await message.answer("Kerakli buyruqni tanlang", reply_markup=markup)


@dp.message_handler(commands='Menu')
async def menu_show(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = KeyboardButton("/Buyurtmalarim")
    bt2 = KeyboardButton("/Lokatsiya", request_location=True)
    bt3 = KeyboardButton("ortga")
    kb.add(bt1)
    kb.add(bt2, bt3)
    await message.answer('Davom eting..', reply_markup=kb)


@dp.message_handler(commands='Buyurtmalarim')
async def orders_show(message: types.Message):
    await message.answer("Sizda buyurtmalar mavjud emas ")


@dp.message_handler(commands='Admin')
async def admin_show(message: types.Message):
    await message.bot.send_contact(message.from_user.id, '998931174113', 'Foziljon')


@dp.message_handler(commands='Sozlamalar')
async def settings_show(message: types.Message):
    await message.bot.send_message(message.from_user.id, "Sozlamalar 🔨")


@dp.message_handler(commands='Buyurtmalarim')
async def orders(message: types.Message):
    await message.answer('Buyurtmalar mavjud emas')


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def location(message: types.Message):
    await message.answer('Rahmat')


@dp.message_handler(lambda message: message.text == "ortga")
async def handle_back_button(message: types.Message):
    await menu_(message)


@dp.message_handler(commands='users_inline')
async def inline_user(message: types.Message):
    a = Users().see_users()
    k = 0
    all_u = []
    if a:
        for i in a:
            k += 1
            all_u.append([InlineKeyboardButton(''.join(i), callback_data=f"user{k}")])
        ikm = InlineKeyboardMarkup(inline_keyboard=all_u)
        await message.answer("Users", reply_markup=ikm)


@dp.message_handler(commands='users_reply')
async def reply_user(message: types.Message):
    a = Users().see_users()

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    if a:
        for i in a:
            markup.add(f"{''.join(i)}")
        await message.answer("All users", reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

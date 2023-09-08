from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
import logging
# from Takrorlash.2_vazifatelegram_bot.database_ import Exercise, session, User
# from Takrorlash.telegram_bot.database_ import Exercise

from dotenv import load_dotenv

load_dotenv()

Bot_Token = "6657313336:AAFDc1-6r59unMTv3rwI7VB__uH3cK-LqO8"
bot = Bot(Bot_Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start_(message: types.Message):
    check = session.query(User).filter(User.user_id == message.from_user.id).first()
    if not check:
        user1 = User(user_id=message.from_user.id, first_name=message.from_user.first_name,
                     last_name=message.from_user.last_name, username=message.from_user.username,
                     is_bot=message.from_user.is_bot, language=message.from_user.language_code)
        session.add(user1)
        session.commit()
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Filiallar📍"), KeyboardButton('Start train🏋'))
    markup.add(KeyboardButton("Admin☎"), KeyboardButton('Nearest location📍', request_location=True))
    await message.answer("FitnessHall ga xush kelibsiz", reply_markup=markup)


@dp.message_handler(Text("Admin☎"))
async def admin_(message: types.Message):
    await message.bot.send_contact(message.from_user.id, "+998931174113", "Foziljon", "Imonqulov")


@dp.message_handler(Text("Filiallar📍"))
async def send_branch(message: types.Message):
    lat = session.query(User).filter(User.user_id == message.from_user.id).first()
    long = session.query(User).filter(User.user_id == message.from_user.id).first()
    await message.bot.send_location(message.from_user.id, latitude=41.322826, longitude=69.283473)


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location(message: types.Message):
    await message.answer('Biz online xizmat korsatamiz😅')


@dp.message_handler(lambda message: message.text in ('Start train🏋'))
async def start_train(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Woman👩"), KeyboardButton("Man👨"))
    markup.add("back🔙")
    await message.answer('Kerakli tugmani tanlang', reply_markup=markup)


@dp.message_handler(Text("back🔙"))
async def back_(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Filiallar📍"), KeyboardButton('Start train🏋'))
    markup.add(KeyboardButton("Admin☎"), KeyboardButton('Nearest location📍', request_location=True))
    await message.answer("Welcome to FitnessHall", reply_markup=markup)


@dp.message_handler(Text("Woman👩"))
async def woman(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton('1-month'), KeyboardButton('2-month'))
    markup.add(KeyboardButton('3-moth'), KeyboardButton('4-mont'))
    markup.add(KeyboardButton('🔙back'))
    await message.answer_photo('https://telegra.ph/file/ed7dc180001c807a07957.png', reply_markup=markup,
                               caption="Quydagilardan birini tanlang")


@dp.message_handler(Text("Man👨"))
async def woman(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton('1-month'), KeyboardButton('2-month'))
    markup.add(KeyboardButton('3-moth'), KeyboardButton('4-mont'))
    markup.add(KeyboardButton('🔙back'))
    await message.answer_photo('https://telegra.ph/file/e118dfb0f00990c6d941b.png', reply_markup=markup,
                               caption="Quydagilardan birini tanlang")


@dp.message_handler(lambda message: message.text in ('1-month', '2-month', '3-moth', '4-month'))
async def train(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Mon'), KeyboardButton('Tues'), KeyboardButton('Wed'))
    markup.add(KeyboardButton('Thur'), KeyboardButton('Fri'), KeyboardButton('Sun'))
    markup.add(KeyboardButton('🔙back'))
    await message.answer('Week day?', reply_markup=markup)


@dp.message_handler(lambda message: message.text in ('Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sun'))
async def train(message: types.Message):
    for i in range(1, 11):
        user = session.query(Exercise).where(Exercise.id == i).first()
        await message.bot.send_animation(message.from_user.id, f"{user.exercise}",
                                         caption="Holatingizga qarab bemalol mashq najaravering")


@dp.message_handler(commands='send')
async def send(message: types.Message):
    for i in range(1, 11):
        user = session.query(Exercise).where(Exercise.id == i).first()
        await message.bot.send_animation(message.from_user.id, f"{user.exercise}",
                                         caption="Holatingizga qarab bemalol mashq najaravering")


@dp.message_handler(Text('🔙back'))
async def back(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Woman👩"), KeyboardButton("Man👨"))
    markup.add("🔙back")
    await message.answer('Kerakli tugmani tanlang', reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

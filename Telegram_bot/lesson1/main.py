from aiogram import Bot, Dispatcher, types, executor
from postgres1 import Users
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

BOT_TOKEN = "6593693542:AAHZNVVPju5nesUbB6HnL0RJoflI-HKx5qM"

bot = Bot(BOT_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    valuess = message.from_user.values
    a = tuple(valuess.values())
    obj = Users(*a)
    obj.insert_into()
    text = f"Hi {message.from_user.first_name} ! Welcome to My bots"
    await message.answer(text)


@dp.message_handler(commands='users_inline')
async def inline_user(message: types.Message):
    a = Users().see_users()
    k = 0
    all_u = []
    for i in a:
        k += 1
        all_u.append([InlineKeyboardButton(''.join(i), callback_data=f"user{k}")])
    ikm = InlineKeyboardMarkup(inline_keyboard=all_u)
    await message.answer("Users", reply_markup=ikm)


@dp.message_handler(commands='users_reply')
async def reply_user(message: types.Message):
    a = Users().see_users()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in a:
        markup.add(f"{''.join(i)}")
    await message.answer("All users", reply_markup=markup)


#
# @dp.message_handler(commands="info")
# async def info_handler(message: types.Message):
#     bot_info = await bot.get_me()
#     await message.answer(str(bot_info))
#
#
# @dp.message_handler(commands="answer")
# async def answer_handler(message: types.Message):
#     await message.answer("This is answer method")

#
# @dp.message_handler(commands="reply")
# async def reply_handler(message: types.Message):
#     await message.reply('Salom! reply')
#
#
# @dp.message_handler(commands="send_message")
# async def send_message_handler(message: types.Message):
#     await message.bot.send_message(message.from_user.id, f"{message.from_user.first_name}:{'salom '}")
#
#
# @dp.message_handler(commands="send_photo")
# async def send_photo(message: types.Message):
#     await message.bot.send_photo(message.from_user.id, "https://telegra.ph/file/5ca7d6968714201ce0ddf.jpg",
#                                  caption='PDP')
#
#
# @dp.message_handler(commands="send_video")
# async def send_video(message: types.Message):
#     await message.bot.send_video(message.from_user.id, "https://t.me/navbaxor_navbahor_fcnavbahor/2714")
#
#
# @dp.message_handler(commands="send_contact")
# async def send_video(message: types.Message):
#     await message.bot.send_contact(message.from_user.id, "998931174113", "Foziljon", "Imonqulov")
#
#
# @dp.message_handler(commands="send_location")
# async def send_video(message: types.Message):
#     await message.bot.send_location(message.from_user.id, 23.45, 24.34)
#
#
# @dp.message_handler(commands="document")
# async def send_document(message: types.Message):
#     await message.bot.send_document(message.from_user.id, open('q.pdf', 'rb'))
#
#
# @dp.message_handler(commands="send_audio")
# async def send_audio(message: types.Message):
#     await message.bot.send_audio(message.from_user.id, audio=open('cinsport.mp3', 'rb'))


# @dp.message_handler(commands="copy")
# async def copy_message(message: types.Message):
#     chat_id = message.chat.id
#     message_id = message.message_id
#     try:
#         copied_message = await bot.copy_message(chat_id=chat_id, from_chat_id=chat_id, message_id=message_id)
#
#         await message.bot.send_message("Xabar nusxalandi!")
#
#     except Exception as e:
#         await message.bot.send_message(f"Xatolik yuz berdi: {e}")

#
# @dp.message_handler()
# async def echo_handler(message: types.Message):
#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

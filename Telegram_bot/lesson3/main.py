import logging
from datetime import timedelta
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text

from Telegram_bot.lesson3.send import insta_downloader, yout_tube_downloader

BOT_TOKEN = '6593693542:AAHZNVVPju5nesUbB6HnL0RJoflI-HKx5qM'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

datas1 = [
    {
        "msg": "salom",
        "reply_msg": "Hi"}
]

badwords = ["yaramas", "jinursin", "block", "axmoq", 'tentak']
block = []


@dp.message_handler(commands='start')
async def any_message(message: types.Message):
    await message.answer("Assalomu alaykum bu bot oraqli siz videolarni yuklab olsihingiz mumkun")


@dp.message_handler(Text(startswith=("https://www.instagram.com/")))
async def send_media(messgae: types.Message):
    link = messgae.text
    data = insta_downloader(link=link)
    try:

        if data == 'Bad':
            await messgae.answer('BU manzil orqli malumot topilmadi')
        else:
            if data['type'] == 'image':
                await messgae.answer_photo(photo=data['media'])
            elif data['type'] == 'video':
                await messgae.answer_video(video=data['media'])
            elif data['type'] == 'carousel':
                for i in data['media']:
                    await messgae.answer_document(document=i)
            else:
                await messgae.answer("Malumotlar tog'ri kelmadi")
    except Exception as e:
        await messgae.answer('')


@dp.message_handler(Text(startswith=("https://www.youtube.com/")))
async def send_video(message: types.Message):
    videoId = message.text
    data = yout_tube_downloader(videoId=videoId)
    try:

        await message.answer_video(video=data['url'])
    except Exception as e:
        await message.answer('Bunday manba topilmadi')


# @dp.message_handler(lambda msg: msg.from_user.id in block)
# async def delete_msg(message: types.Message):https://www.youtube.com/watch?v=r9q-muqhLIA
#     await message.delete()


@dp.message_handler()
async def any_message(msg: types.Message):
    for i in msg.text.split():
        if i in badwords:
            await msg.delete()
            await msg.answer(f"Iltimos haqoratli so'z ishlatilmasin ! {msg.from_user.first_name}")
            # await bot.ban_chat_member(msg.chat.id, msg.from_user.id, ChatPermissions(can_change_info=False))
            # block.append(msg.from_user.id)


@dp.message_handler()
async def any_message(msg: types.Message):
    l = []
    for i in datas1:
        if msg.text == i.get("msg"):
            l.append(i.get("reply_msg"))

    if not l:
        if msg.reply_to_message:
            info = {
                "msg": msg.reply_to_message.text,
                "reply_msg": msg.text
            }
            datas1.append(info)
    else:
        await msg.reply(l[-1])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

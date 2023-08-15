# from aiogram import Bot, Dispatcher, types, executor
# import img2pdf
# import fpdf as FPDF
# from PIL import Image
# import os
#
# bot_token = "6593693542:AAHZNVVPju5nesUbB6HnL0RJoflI-HKx5qM"
#
# bot = Bot(bot_token)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start'])
# async def start_bot(message: types.Message):
#     text = f"Assalomu alaykum {message.from_user.first_name} Image to Pdf botiga xush kelibsiz"
#     await message.answer(text)
#     await message.answer('Botdan foydalanish uchun rasmlarni yuboring')
#
#
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def convert_to_pdf(message: types.Message):
#
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)

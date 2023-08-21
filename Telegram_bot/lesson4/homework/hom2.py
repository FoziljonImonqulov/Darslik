import requests
from bs4 import BeautifulSoup

from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

bot_token = "6593693542:AAHZNVVPju5nesUbB6HnL0RJoflI-HKx5qM"

bot = Bot(bot_token)

dp = Dispatcher(bot)


def courses():
    response = requests.get("https://namozvaqtlari.com/")
    html = response.content.decode()
    soup = BeautifulSoup(html, 'html.parser')
    datas = []

    for i in soup.find_all('div', {'class': 'box box1'}):
        d = {'title': i.find('h2').text,
             'time': i.find('p').text,
             'place': i.find('div', {'class': 'h3'}).text,
             'image': i.find('div', {'class': 'image'}).img['src']}
        datas.append(d)
    return datas


courses()


@dp.message_handler(commands='/time')
async def start_(message: types.Message):
    await message.answer("Kunlik namoz vaqtlarini bilib oling!")
    data = courses()
    markup = InlineKeyboardMarkup()
    for i in range(len(data)):
        markup.add(
            InlineKeyboardButton(f"{data[i]['title']} : {data[i]['time']}", callback_data=f"{data[i].get('title')}"))

    await message.bot.send_photo(chat_id=message.from_user.id,
                                 photo=f"https://namozvaqtlari.com/{data[0].get('image')}", reply_markup=markup)

    im = data[1]['image']
    # await message.bot.send_photo(message.from_user.id, f"https://namozvaqtlari.com/{data[0].get('image')}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

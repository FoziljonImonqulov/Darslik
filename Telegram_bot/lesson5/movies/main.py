import requests
from bs4 import BeautifulSoup
import time
response = requests.get("http://uzmovi.com")
html = response.content.decode()
soup = BeautifulSoup(html, 'html.parser')
from aiogram import Bot, types, executor, Dispatcher

bot_token = "6593693542:AAHZNVVPju5nesUbB6HnL0RJoflI-HKx5qM"

bot = Bot(bot_token)

dp = Dispatcher(bot)

movies = []


def main_():
    for i in soup.find_all('div', {'class': 'short-images radius-3'})[:5]:
        m = {
            'movie_image_link': i.find('a', {'class': 'short-images-link'}).img['data-src'],
            'movie_title': i.find('a', {'class': 'short-images-link'}).img['alt'],
            'movie_link': i.a['href']}
        movies.append(m)

    return movies


main_()


@dp.message_handler(commands='movies')
async def get_last_one(message: types.Message):
    await message.answer("See latest movies in the world")
    all_one = main_()
    for i in all_one:
        time.sleep(5)
        text = f"""
        {i.get('movie_title')}


[See movie]({i.get('movie_link')})
"""
        await message.bot.send_photo(-1001909378622, i.get('movie_image_link'), caption=text,parse_mode='Markdown')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

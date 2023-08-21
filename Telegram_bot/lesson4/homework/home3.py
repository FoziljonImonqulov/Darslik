import requests
from bs4 import BeautifulSoup

response = requests.get("https://qalampir.uz/")
html = response.content.decode()
soup = BeautifulSoup(html, 'html.parser')
from aiogram import Bot, types, executor, Dispatcher

bot_token = "6593693542:AAHZNVVPju5nesUbB6HnL0RJoflI-HKx5qM"

bot = Bot(bot_token)

dp = Dispatcher(bot)

news = []


def main_():
    for i in soup.find_all('div', {'class': 'col-md-6 last-news-card'})[:5]:
        info = {'news_link': i.a['href'],
                'news_image': i.find('a', {'class': 'news-card-img'}).img['src'],
                'news_title': i.find('a', {'class': 'news-card-img'}).img['alt'],
                'news_date': i.find('span', {'class': 'date'}).text}
        news.append(info)
    return news


@dp.message_handler(commands='news')
async def get_last_one(message: types.Message):
    await message.answer("See last news in the world")
    all_one = main_()
    for i in all_one:
        text = f"""
        {i.get('news_title')}

{i.get('news_date')}

({i.get('news_link')})
"""
        await message.bot.send_photo(-1001909378622, i.get('news_image'), caption=text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

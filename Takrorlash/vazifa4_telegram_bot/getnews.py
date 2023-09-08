import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.fitnessblender.com/")
html = response.content.decode()
soup = BeautifulSoup(html, 'html.parser')

movies = []


def main_():
    for i in soup.find_all('section', {'class': '-card-view'}):
        title_name = i.find('div', {'class': 'group responsive-media'}).img['data-src']
        print(title_name)


    #     m = {
    #         'movie_image_link': i.find('a', {'class': 'short-images-link'}).img['data-src'],
    #         'movie_title': i.find('a', {'class': 'short-images-link'}).img['alt'],
    #         'movie_link': i.a['href']}
    #     movies.append(m)
    #
    # return movies


main_()

#
# @dp.message_handler(commands='movies')
# async def get_last_one(message: types.Message):
#     await message.answer("See latest movies in the world")
#     all_one = main_()
#     for i in all_one:
#         text = f"""
#         {i.get('movie_title')}
#
#
# [See movie]({i.get('movie_link')})
# """
#         await message.bot.send_photo(-1001909378622, i.get('movie_image_link'), caption=text)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)

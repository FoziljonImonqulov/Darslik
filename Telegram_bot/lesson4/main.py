# import datetime
#
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("https://daryo.uz/yangiliklar")
#
# html = response.content.decode()
#
# soup = BeautifulSoup(html, 'html.parser')
# data = []
# for i in soup.find_all('div', {'class': 'mini__article'})[:4]:
#     data.append({"title": i.h3.text,
#                  "photo_link": i.find("a", {'class': "border mini__article-img"}).img['data-src'],
#                  "timee": f"{datetime.datetime.now()},{i.time.text.split(',')[-1]}"})


# print(soup.prettify())
#
# # for i in soup.find_all("div",{"class":""})
# for i in soup.find_all("li", {"class": "menu__layout_unit"}):
#     dat = i.a['href']
#     data = requests.get(f"{dat}")
#     html = data.content.decode()
#     soup = BeautifulSoup(html, 'html.parser')
#     file = soup.prettify()
#     name = dat.split('/')[-1]
#     with open(f"{name}", 'w') as f:
#         f.write(file)

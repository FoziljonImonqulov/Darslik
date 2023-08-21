import requests
from bs4 import BeautifulSoup

response = requests.get("https://online.pdp.uz/profile/all-courses")

html = response.content.decode()

soup = BeautifulSoup(html, 'html.parser')


def courses():
    for i in soup.find_all('div', {'class': 'col-table col-md-6'}):
        link = i.a['href']
        name = i.find('a', {'class': "text-decoration-none"})
        print(link.text)


courses()

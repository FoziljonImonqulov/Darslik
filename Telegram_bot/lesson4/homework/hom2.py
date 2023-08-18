import requests
from bs4 import BeautifulSoup

response = requests.get("https://namozvaqtlari.com/")

html = response.content.decode()

soup = BeautifulSoup(html, 'html.parser')


def courses():
    for i in soup.find_all('div', {'class': 'nomoz-time'}):
        print(i.h3['title'])


courses()

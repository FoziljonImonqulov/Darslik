import requests
from bs4 import BeautifulSoup

response = requests.get("https://online.pdp.uz/")

html = response.content.decode()

soup = BeautifulSoup(html, 'html.parser')


def courses():
    print(soup)


courses()

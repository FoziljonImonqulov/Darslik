from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">Salom</p>
<p class="story2">Salom</p>
<p class="story">Salom</p>"""

soup = BeautifulSoup(html_doc, 'html.parser')

# for i in soup.find_all("a", {"href": "http://example.com/elsie"}):
#     print(i.text)

# for i in soup.find_all("p", {"class": "story2"}):
#     print(i.text)
#

# print(soup.p['class'])
# for i in soup.find_all("a"):
#     print(i['href'])

print(soup.get_text())
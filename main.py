import bs4
import requests
from fake_headers import Headers
from funcs import time, header, link, check_article, text_article


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/articles/'
response = requests.get(url,
    headers=Headers(browser='chrome', os='mac').generate())

soup = bs4.BeautifulSoup(response.text, features='lxml')
items = soup.select('div.tm-article-snippet')

for i in items:
    if check_article(KEYWORDS, i):
        print(time(i), header(i), link(i), sep=" -- ")
        print('\n'.join(text_article(i)))

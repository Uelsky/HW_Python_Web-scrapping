import re
from re import findall

import bs4


def time(article: bs4.element.Tag) -> str:
    return article.select('time')[0].attrs['title']


def header(article: bs4.element.Tag) -> str:
    return article.select('span')[2].text


def link(article: bs4.element.Tag) -> str:
    article_url = 'https://habr.com' + article.select('a')[2].attrs['href']

    return article_url


def text_article(article: bs4.element.Tag):
    step1 = article.find('div', class_='article-formatted-body')
    step2 = step1.findAll('p')
    result = list(map(lambda x: x.text, step2))
    return result


def check_article(keywords: list, article: bs4.element.Tag) -> bool:
    ans = False

    for word in keywords:
        if re.findall(word, article.text):
            ans = True
            break

    return ans
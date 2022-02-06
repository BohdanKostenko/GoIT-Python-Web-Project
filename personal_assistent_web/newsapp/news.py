import requests
from bs4 import BeautifulSoup

# news from BBC
bbc_cls = "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor"


def bbc_tech():
    url = "https://www.bbc.com/news/technology"
    req = requests.get(url, headers={'User-Agent': 'Mozilla'})
    soup = BeautifulSoup(req.content, 'html.parser')
    result = soup.find(
        'a', class_=bbc_cls).get('href')
    link = f'https://www.bbc.com{result}'
    text = soup.find(
        'a', class_=bbc_cls).text
    return link, text, "(bbc.com)"


def bbc_sceince():
    url = "https://www.bbc.com/news/science_and_environment"
    req = requests.get(url, headers={'User-Agent': 'Mozilla'})
    soup = BeautifulSoup(req.content, 'html.parser')
    result = soup.find(
        'a', class_=bbc_cls).get('href')
    link = f'https://www.bbc.com{result}'
    text = soup.find(
        'a', class_=bbc_cls).text
    return link, text, "(bbc.com)"


def bbc_health():
    url = "https://www.bbc.com/news/health"
    req = requests.get(url, headers={'User-Agent': 'Mozilla'})
    soup = BeautifulSoup(req.content, 'html.parser')
    result = soup.find(
        'a', class_=bbc_cls).get('href')
    link = f'https://www.bbc.com{result}'
    text = soup.find(
        'a', class_=bbc_cls).text
    return link, text, "(bbc.com)"


def bbc_sport():
    url = "https://www.bbc.com/sport"
    req = requests.get(url, headers={'User-Agent': 'Mozilla'})
    soup = BeautifulSoup(req.content, 'html.parser')
    link = soup.find(
        'a',
        class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link sp-o-link-split__anchor gel-double-pica-bold').get(
        'href')
    text = soup.find(
        'a',
        class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link sp-o-link-split__anchor gel-double-pica-bold').text
    link = f'https://www.bbc.com{link}'
    return link, text, "(bbc.com)"


# news from Liga.net

def liga_tech():
    url = "https://tech.liga.net/ua"
    req = requests.get(url, headers={'User-Agent': 'Mozilla'})
    link = BeautifulSoup(req.text, 'lxml').find(
        'div', class_='hidden-xs hidden-sm visible-md visible-1k').find('li').find('a').get('href')
    text = BeautifulSoup(req.text, 'lxml').find(
        'div', class_='hidden-xs hidden-sm visible-md visible-1k').find('li').find('a').text
    return link, text, "(liga.net)"


def liga_sceince():
    url = "https://life.liga.net/tag/naukpop"
    req = requests.get(url, headers={'User-Agent': 'Mozilla'})
    soup = BeautifulSoup(req.text, 'lxml')
    link = soup.find(
        'div', class_='news-block-img big-list-article').find('a').get('href')
    text = soup.find(
        'div', class_='news-text').text
    return link, text, "(liga.net)"


def liga_health():
    url = "https://life.liga.net/tag/zdorovya"
    req = requests.get(url, headers={'User-Agent': 'Mozilla'})
    soup = BeautifulSoup(req.text, 'lxml')
    link = soup.find(
        'div', class_='news-block-img big-list-article').find('a').get('href')
    text = soup.find(
        'div', class_='news-text').text
    return link, text, "(liga.net)"


def liga_sport():
    url = "https://life.liga.net/tag/sport"
    req = requests.get(url, headers={'User-Agent': 'Mozilla'})
    soup = BeautifulSoup(req.text, 'lxml')
    link = soup.find(
        'div', class_='news-block-img big-list-article').find('a').get('href')
    text = soup.find(
        'div', class_='news-text').text
    return link, text, "(liga.net)"


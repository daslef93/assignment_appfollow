'''
Парсинг | 10 *
Напишите программу на Python 3, которая будет при запуске сохранять список
заголовков текущих новостей с главной страницы сайта yandex.ru
(те, что выше поисковой строки) в текстовый документ в папке нахождения программы
в формате 1 заголовок = 1 строка. В приложении приложите текст программы или ссылку на файл программы
'''

import time
import requests
from bs4 import BeautifulSoup, FeatureNotFound
from typing import List


def parse(mode='top_four') -> List[str]:
    '''
    пятая строка топа - динамическая, включает в себя вложенный ненумерованный список;
    в режиме top_four она игнорируется;
    '''

    r = requests.get('http://yandex.ru')

    try:
        soup = BeautifulSoup(r.text, 'lxml')
    except FeatureNotFound:
        soup = BeautifulSoup(r.text, 'html.parser')
        
    top_news_wrapper = soup.select('.news__panels.mix-tabber-slide2__panels')

    if mode == 'top_five':
        top_news = [i.text for i in top_news_wrapper[0].select('li.list__item span.news__item-content')]
    elif mode == 'top_four':
        top_news = [i.text for i in top_news_wrapper[0].select('ol')[0].select('li.list__item span.news__item-content')]

    return top_news

def save_to_file(news: List[str]) -> None:
    
    timestamp = time.strftime("%Y_%m_%d_%H_%M", time.localtime())

    try:
        with open(f'output_{timestamp}.txt', 'w') as f:
            f.write('\n'.join(news))
    except Exception as e:
        print(e)
    else:
        print('File was succesfully written')


if __name__ == '__main__':
    save_to_file(parse("top_five"))

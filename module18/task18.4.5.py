# Допишите сделанный ранее скрипт (где мы доставали заголовки новостей о Python с Python.org) так, чтобы он показывал
# ещё и дату добавления новости.
# Примечание: Для получения атрибутов тега (т. е. его дополнительных параметров) используется метод .get(<имя атрибута>).

import requests
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content

tree = lxml.html.document_fromstring(html)

ul = tree.findall('body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')

for li in ul:
    a = li.find('a')
    date = li.find('time').get('datetime')
    print(date[0:10:] + ' ' + a.text)
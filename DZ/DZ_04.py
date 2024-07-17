"""Выберите веб-сайт с табличными данными, который вас интересует.
Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

Ваш код должен включать следующее:

Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
Комментарии для объяснения цели и логики кода.

Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге."""

import requests
from lxml import html
import pandas as pd
import csv

url = "https://www.atptour.com/en/rankings/singles"

response = requests.get(url, headers={
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
tree = html.fromstring(response.content)
"""print(tree)

table_rows = tree.xpath("//table[@class='mobile-table mega-table non-live']/tbody/tr")
columns = table_rows[0].xpath(".//td/text()")
for col in columns:
    print(col)
col_names = tree.xpath("//table[@class='mobile-table mega-table non-live']/thead/tr/text()")
for col_name in col_names:
    print(col_name)"""

table_rows = tree.xpath("//table[@class='mobile-table mega-table non-live']/tbody/tr")
list_data = []
for row in table_rows:
    columns = row.xpath(".//td/text()")
    list_data.append({
        'rank': columns[0].strip(),
        'player': columns[2].strip(),
        'Official Points': columns[3].strip()
    })
    #print(list_data)
    df = pd.DataFrame(list_data)
    print(df)
    


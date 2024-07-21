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


url = "https://finance.yahoo.com/trending-tickers/?guccounter=1&guce_referrer=aHR0cHM6Ly9lZHUubGl2ZWRpZ2l0YWwuc3BhY2Uv&guce_referrer_sig=AQAAADGHJGtm3-4AUeC5nljuKtS_fiU1h8Qp4xlyIwrpiyYKPxo59E-QsLol8eJ5Mws0P0mUew9a19MP_dXQTFJVPLDag86uVKwQ5iWUyOSFdinelpbQ_QfSFm5YHaSH6aNhcbprdYXBw2GaKrxdYTFQFm7HivjPfyjOHUUNJR6J2YOb"

response = requests.get(url, headers={
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

# https://pypi.org/project/fake-useragent/ 

tree = html.fromstring(response.content)
print(tree)

table_rows = tree.xpath("//table[@class='W(100%)']/tbody/tr")
list_data = []
for row in table_rows:
    columns = row.xpath(".//td/text()")
    list_data.append({
        'Symbol': row.xpath(".//td/a/text()")[0].strip(),
        'Name': columns[0].strip(),
        'Last Price':  int(row.xpath(".//td/fin-streamer/text()")[0].replace(',', '').replace('.', '').strip()),
        'MarketTime':  row.xpath(".//td/fin-streamer/text()")[1].strip(),
        'Change': row.xpath(".//td/fin-streamer/span/text()")[0].strip(),
        '% Change': row.xpath(".//td/fin-streamer/span/text()")[1].strip(),
        'Volume': row.xpath(".//td/fin-streamer/text()")[2].strip(),        
        })
    #print(list_data)
    df = pd.DataFrame(list_data)
    df.to_csv('list_data.csv')
    print(df)
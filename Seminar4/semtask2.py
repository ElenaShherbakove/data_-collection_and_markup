import requests
from lxml import html
import pandas as pd

url = "https://www.worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page=1"

response = requests.get(url, headers={
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

# https://pypi.org/project/fake-useragent/ 

tree = html.fromstring(response.content)
print(tree)

table_rows = tree.xpath("//table[@class='records-table']/tbody/tr")
list_data = []
for row in table_rows:
    columns = row.xpath(".//td/text()")
    list_data.append({
        'rank': columns[0].strip(),
        'mark': columns[1].strip(),
        'WIND': columns[2].strip(),
        'WIND1': columns[3].strip(),
        'Competitor': row.xpath(".//td[4]/a/text()")[0].strip(),
        'DOB': columns[5].strip(),
        'NAT': columns[7].strip(),
        'POS': columns[8].strip(),
        'VENUE': columns[9].strip(),
        'Date': columns[10].strip(),
        'Result_Score': columns[11].strip(),
    })
    print(list_data)
    df = pd.DataFrame(list_data)
    print(df)

import requests
# отправка GET-запроса на конечную точку REST API
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# проверка успешности выполнения запроса
if response.status_code == 200:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)

    # отправка POST-запроса на конечную точку REST API
data = {
    "title": "УРА",
    "body": "Scraping",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

# проверка успешности выполнения запроса
if response.status_code == 201:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)

payload = {"field1": "value1", "field2": "value2"}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=payload)

# проверка успешности выполнения запроса
if response.status_code == 200:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)

    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

# проверка успешности выполнения запроса
if response.status_code == 200:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)
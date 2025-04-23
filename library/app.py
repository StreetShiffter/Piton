import logging
import json
import requests
import datetime

# Ваш API-ключ
API_KEY = 'dccd05a351f4428fb86b0d3343b299ef'
# URL API
URL = 'https://newsapi.org/v2/everything'


def info_news(data_input, api_key):
    today = datetime.datetime.today()

    # Параметры запроса
    params = {
        'q': data_input,
        'from': today.strftime('%Y-%m-%d'),
        'sortBy': 'publishedAt',
        'apikey': api_key
    }

    # Выполнение GET-запроса
    response = requests.get(url=URL, params=params)

    # Обработка ответа
    if response.status_code == 200:
        # Если запрос успешен, выводим данные
        print(response.json())
    else:
        # Если произошла ошибка, выводим код ошибки и сообщение
        print(f"Ошибка: {response.status_code} - {response.text}")


# Вызов функции
info_news('Python programming', API_KEY)
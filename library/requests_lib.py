import requests


MY_API_KEY = 'd5ba4b9dd46e8a25fc96433451ecf192' #Уникальный API для https://openweathermap.org/api/geocoding-api

rasp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q=Novosibirsk&appid={MY_API_KEY}') # запрос для геолокации

#print(rasp.json()) - получение данных города

lat = rasp.json()[0]['lat'] # указываем [0] т.к. мы указали только один город - 1(если получаем индекс второго ) и т.д.
lon = rasp.json()[0]['lon']

weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={MY_API_KEY}')

print(weather.json())

# Декоратор для обработки исключений
# def exception_handler(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except requests.exceptions.RequestException as e:
#             print(f"Обнаружена ошибка: {e}")
#             return None
#     return wrapper
#
# # Функция, обернутая декоратором
# @exception_handler
# def fetch_data(url):
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.text
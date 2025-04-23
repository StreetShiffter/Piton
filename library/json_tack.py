import json



book = {
    'title':'Pasha Technik and plushka',
    'author':'RAP family',
    'publication_year': 2025,
    'genre':['autobiografy', 'triller']
}

json_books = json.dumps(book)# перевод объекта PY в JSON строку
json_books_2 = json.dumps(book,indent = 25)# создание дополнительных отступов
json_books_3 = json.dumps(book,sort_keys=True)# сортировка ключей по алфавиту
print(json_books_3)

data_copy = json.loads(json_books) # перевод JSON строки в объект PY
# print(data_copy)


with open('json_books.json','w') as file:
    json.dump(book, file) # записываем словарь book в файл 'json_books.json'


with open('json_books.json') as file1:
    data_copy_file = json.load(file1) # подгружаем из json данные в file1 и записываем в переменную data_copy
# print(data_copy_file)

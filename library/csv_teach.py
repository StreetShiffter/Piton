import csv

rows = [['Name', 'Age', 'Gender'],
        ['Alice', '25', 'Female'],
        ['Bob', '30', 'Male'],
        ['Charlie', '35', 'Male']]

# with open('file.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(rows) # запись всех строк

# with open('file.csv', 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(rows[1]) # запись конкретной строки

# with open('file.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row) # правильное чтение

with open('file.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row) # чтение как словарь



import csv

with open('..\students.csv') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # Пропускаем заголовок таблицы
    for row in reader:
        name, age, avg_grade = row
        if float(avg_grade) > 4.5:
            print(f'{name} ({age} лет) - средний балл: {avg_grade}')
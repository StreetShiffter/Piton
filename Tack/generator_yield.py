# def infinite_sequence(start=1):
#     while True:
#         yield start
#         start += 1
#
# numbers = infinite_sequence()
# a = next(numbers)
# b = next(numbers)
# calc = a + b
# print(calc)
#
#
# numbers = [10, 20, 30, 40]
# # Получаем итератор для списка
# iterator = iter(numbers)
#
# # Используем next() для получения следующего элемента из итератора
# print(next(iterator))  # Выведет 10
# print(next(iterator))  # Выведет 20
# print(next(iterator))  # Выведет 30
# print(next(iterator))  # Выведет 40
#
# def f():
#     print('Initializing...')
#     yield 'one'
#     print('Continue...')
#     yield 'two'
#     print('Stopping...')
#
# i = f()
# try:
#     print(next(i))
#     print(next(i))
#     print(next(i))
# except StopIteration:
#     print("Генератор завершил свою работу.")

# Напишите генераторное выражение, которое возвращает кубы четных чисел от 0 до 10.

# num_cub = (x**3 for x in range(1,11) if x % 2 == 0)
# print(*(num_cub))

# Напишите функцию, которая принимает список чисел и возвращает сумму квадратов положительных чисел в этом списке.
# Используйте для этого генераторное выражение.

# def calculation_sqware(nums):
#     return sum(x**2 for x in nums if x>0)
#
# nums_list = [2, 7, 9, -5, 7, 0, -1]
# print(calculation_sqware(nums_list))

# Напишите генераторное выражение, которое возвращает буквы строки "hello", но только если они являются гласными.

# vowels = (x for x in "hello" if x in ['a', 'e', 'i', 'o', 'u'])
# print(*(vowels))

# Найдите среднее арифметическое всех чисел, кратных 3 или 5, в заданном диапазоне.

# total = [x for x in range(1, 101) if x % 3 == 0 or x % 5 ==0 if x != 0]
# result = sum(total) / len(total)
# print(result)

# numbers = range(1, 101)
# filtered_numbers = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))
# average = sum(filtered_numbers) / len(filtered_numbers)
# print(average)

# Объедините несколько списков в один список, учитывая возможные дубликаты элементов.
# list_1 = [1, 3, 5, 7, 9]
# list_2 = [2, 3, 4, 6, 9, 8]
# new_list = set(list_1 + list_2)
# print(sorted(new_list))

# from itertools import chain
#
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# list3 = [5, 6, 7, 8]
# combined_list = list(set(chain(list1, list2, list3)))
# print(combined_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


# Дан список словарей. Отфильтруйте его по ключу age и значению 30

# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 35},
#     {"name": "David", "age": 30},
#     {"name": "Eve", "age": 25},
# ]
# result = [x for x in people if x.get("age") == 30]
# print(result)
#
# result = list(filter(lambda x: x.get("age") == 30, people))
# print(result)

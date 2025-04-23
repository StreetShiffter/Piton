import time
from datetime import datetime
from functools import wraps
from time import ctime




def valid(filename=None):
    """Декоратор для измерения времени выполнения функции и логирования."""

    def decor(words):
        @wraps(words)
        def value(*args, **kwargs):
            time_total = None  # Инициализация переменной для времени выполнения
            try:
                time1 = ctime()
                # time1 = datetime.now()
                # time0 = time.perf_counter() # чек времени
                result = words(*args, **kwargs)  # Вызов оригинальной функции
                time2 = time.perf_counter()
                # time_total = round(time2 - time0)  # Вычисление времени выполнения

                # Запись информации о выполнении функции в файл или вывод
                log_message = f"Записан {words.__name__}, {time1}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f'{log_message} \n')
                else:
                    print(log_message)

                return result  # Возвращаем результат работы функции

            except Exception as fail:
                error_message = f"Записан {words.__name__}, Error: {type(fail).__name__}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        # Запись ошибки в файл
                        file.write(error_message + "\n")
                else:
                    print(error_message)

                # Повторно возбуждаем исключение
                raise

        return value

    return decor

@valid(filename='Loginorov.txt')
def intersection_list(list_a, list_b):
    """Функция для получения одинаковых чисел"""
    set_a = set(list_a)
    set_b = set(list_b)
    if not set_a or not set_b:
        raise ValueError("Один из списков пуст. Нет значений для пересечения.")
    else:
        int_list = list(set_a.intersection(set_b))

    return int_list


list_a = [3, 4, 5, 6,456,657,87,3,23,867,98,435,3]
list_b = [3, 4, 5, 6,456,657,87,3,23,867,98,435,3,56,5786,76,45,32,342567,345,5,623,23,34,54,5346,76,546,767]
test = intersection_list(list_a, list_b)
print(test)

# def intersection_list(list_a, list_b):
#     """Функция для получения одинаковых чисел"""
#     set_b = set(list_b)
#     listing = []
#
#     for i in set_b:
#         if isinstance(i, str | float):
#             continue
#         elif i % 2 ==0:
#             listing.append(int(i))
#     return listing
#
#
#
# list_a = [1, 2, 3, 4]
# list_b = [3, 4, 5, 'a', 6, ' ', 3.2, '!', 1, 0, 6]
# test = intersection_list(list_a, list_b)
# print(test)


# def valid(filename):
#     def decorator(words):
#         def value(*args, **kwargs):
#             result = words(*args, **kwargs)
#
#             with open(filename, 'a', encoding='utf-8') as file:
#                 file.write(f'Записан лог {words.__name__}\n')
#             return result
#
#         return value
#     return decorator
#
# @valid(filename='Loginorov.txt')
# def intersection_list(list_a, list_b):
#     """Функция для получения одинаковых чисел"""
#     set_a = set(list_a)
#     set_b = set(list_b)
#
#     int_list = list(set_a.intersection(set_b))
#
#     return int_list
#
# list_a = [1, 2, 3, 4]
# list_b = [3, 4, 5, 6]
# test = intersection_list(list_a, list_b)
#
# # Печатаем результат
# print(test)

"""new_list = []
    for i in list_a:
        if i in list_b:
        new_list.append(i)
        
    return new_list
    
    
 if  __name__ == '__main__':
    print(intersection_list(list_a = [1, 2, 3, 4], list_b = [3, 4, 5, 6])) 
    # в консоли ввести  python3 scr/main.py
    """

"""return [i for i in list_1 if i in list_2]"""

"""a = list(set(list_1)&set(list_2))"""

from functools import wraps
from time import ctime


def write_log(message, filename=None):
    """Записывает сообщение в файл или выводит его на консоль"""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)


def log(filename=None):
    """Декоратор для логирования вызовов функций и возникающих в них ошибок"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            write_log(f"Функция {func.__name__} началась в {ctime()}", filename)


            try:
                result = func(*args, **kwargs)
                write_log(f"Функция {func.__name__} завершилась успешно в {ctime()}", filename)
                return result


            except Exception as e:
                write_log(f"Ошибка в {func.__name__}: {str(e)}", filename)
                raise

        return wrapper
    return decorator
















@log()
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

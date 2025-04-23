def check_integers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Проверка на тип с использованием isinstance()
        if isinstance(result, float):
            return round(result)
        elif isinstance(result, (list, tuple)):
            rounded = [round(x) if isinstance(x, float) else x for x in result]
            # Возвращаем тот же тип, что и исходный (list или tuple)
            return type(result)(rounded)
        else:
            return result

    return wrapper


@check_integers
def numbers(a):
    return a


# Пример использования
a = 3.14
total = numbers(a)
print(total)  # Вывод: 3

# Пример с списком
b = [1.5, 2.8, 3.3]
total_list = numbers(b)
print(total_list)  # Вывод: [2, 3, 3]

# Пример с кортежем
c = (4.6, 5.5, 6.2)
total_tuple = numbers(c)
print(total_tuple)  # Вывод: (5, 6, 6)

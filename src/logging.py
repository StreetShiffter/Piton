from functools import wraps

def logging(func):
    @wraps(func)
    def log(*args, **kwargs):
        result = intersection_list(*args, **kwargs)
        try:
            if filename:
                with open(filename=None, 'a', encoding = 'utf-8') as file:
                    file.write(f'Info module{func} is ok')

            else:
                print(f'Info module{func} is ok')
            return result
        except ValueError:
            if filename:
                with open(filename=None, 'a', encoding='utf-8') as file:
                    file.write(f'Info module{func} error result')

            else:
                print(f'Info module{func} error result')
            return result
    return log




@logging
def intersection_list(list_a: List[int], list_b: List[int]) -> List[int]:
    """Функция для получения одинаковых чисел"""
    set_a = set(list_a)
    set_b = set(list_b)

    int_list = list(set_a.intersection(set_b))

    return int_list


list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
test = intersection_list(list_a, list_b)

print(test)
# def positive_integers(func):
#     def check_values(*agrs):
#         for i in agrs:
#             if not isinstance(i, int):
#                 raise ValueError("All arguments must be positive integers")
#             else:
#                 result = func(*agrs)
#                 return result
#     return check_values


def positive_integers(func):
    def check_values(*agrs):
        for i in agrs:
            if isinstance(i, int) and i > 0:
                result = func(*agrs)
                return result
            else:
                raise ValueError("Все плохо")

    return check_values




@positive_integers
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply("2, 5, 4")) # Вывод: 24
print(multiply(2, 0, 4))

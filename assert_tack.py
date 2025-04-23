def add_numbers(a, b):
    if a > 0 or b > 0:
        return a+b
    return a+b

def is_even(a):
    return a%2 == 0

def find_max(my_list):
    if len(my_list) > 0:
        return max(my_list)
    return 0

if __name__ == '__main__':
    assert add_numbers(2,2) == 4
    assert add_numbers(0, 0) >= 0

    assert is_even(2)

    assert find_max([1, 6, 65, 45, 12, 4, 9]) == 65
    assert find_max([]) == 0
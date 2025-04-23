from typing import List


def difference_list(list_a: List[int], list_b: List[int]) -> List[int]:
    # """Функция возвращающие элементы не повторяющиеся"""
    # return list(set(list_a) - set(list_b)) + list(set(list_b) - set(list_a))
    return set(list_a) ^ set(list_b)


__name__ = "__main__"
print(difference_list([1, 2, 3, 4], [3, 4, 5, 6]))

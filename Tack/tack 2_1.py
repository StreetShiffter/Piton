from typing import List


def intersection_list(list_a: List[int], list_b: List[int]) -> List[int]:
    """Функция для получения одинаковых чисел"""
    set_a = set(list_a)
    set_b = set(list_b)

    #int_list = list(set_a.intersection(set_b))
    #return int_list

    return set_a & set_b


list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
test = intersection_list(list_a, list_b)

print(test)

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

'''a = list(set(list_1)&set(list_2))'''

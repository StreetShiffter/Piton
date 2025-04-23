from itertools import chain

# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = map(lambda x: x * 2, numbers)
# for i in doubled_numbers:
#     print(i)
#
#
# numbers2 = [1, 2, 3, 4, 5]
# dub = [2*i for i in numbers2]
# for r in dub:
#     print(r)

def numbers_double(x):
    return x*2

list_num = [0, 1, 2 ,3 ,4 ,5]

dub_num = map(numbers_double, list_num)
print(list(dub_num))
#
# def predicate(x):
#     if x % 2 ==0:
#         return x
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# filter_num = filter(predicate, numbers)
# print(filter_num)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# chain_numbers = list(chain(list1, list2))
#
# print(list(chain_numbers))
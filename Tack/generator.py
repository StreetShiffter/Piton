from itertools import chain

# def even(x):
#     return x % 2 ==0
#
# def doubling (y):
#     return [y, y]
#
# listing = [0, 1, 2, 3, 4, 5, 6]
#
# filter_list = list(filter(even, listing))
# double_list = map(doubling,filter_list)
# total = [num for i in double_list for num in i]
# print(total)


def even(x):
    return x % 2 == 0


def doubling(y):
    return [y, y]


listing = [0, 1, 2, 3, 4, 5, 6]

filter_list = list(filter(even, listing))
double_list = map(doubling, filter_list)
total = list(chain(*double_list))
print(total)

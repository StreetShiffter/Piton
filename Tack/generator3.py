# def sqare_num(x):
#     return sum(i**2 for i in x)
#
# generator = (i for i in range(1, 101) if i % 2 ==0)
# print(sqare_num(generator))


# generator = (sum(i*i for i in range(1, 101) if i % 2 ==0))
# print(generator)

squares_gen = (x**2 for x in range(5))
print(list(squares_gen))  # Вывод: [0, 1, 4, 9, 16]
# После этой строки gen будет исчерпан, и следующее использование не даст никаких значений:
print(list(squares_gen))

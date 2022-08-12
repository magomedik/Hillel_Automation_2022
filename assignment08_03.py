# Завдання: замінити виклик своєї функції (ітерації та фільтрування елеменів)
#           на використання вбудованої функції filter (використати звичайну
#           або lambda функції як фільтруючу - перший аргумент).
#
# Приклад:
#         ввод: 32 7 0 10 11 78 9 5 23 99
#         результат: 32 0 10 78
#
# Підказки:
#    * filter(callable, iterable)
#


import random

rand_list = random.sample(range(1, 100), 10)


def fun(data):
        x = list(filter(lambda i: i % 2 == 0, data))
        return x


print(fun(rand_list))

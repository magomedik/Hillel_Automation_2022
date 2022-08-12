# Завдання: модіфікувати попередне завдання використавши
#          lambda функції.
#
# Приклад:
#         ввод: 32 7 0 10 11 78 9 5 23 99
#         результат: 32 0 10 78
#
# Підказка:
#   * evens = lambda n: n % 2 == 0 (чи можно одразу передати
#                lambda n: n % 2 == 0 у місці виклиу функції
#                другим аргументом - вона одразу присвоїться
#                в аргумент, але не буде доступна після).


import random

rand_list = random.sample(range(1, 100), 10)

evens = lambda i: i % 2 == 0

def filter(data, evens):
    res = [i for i in data if evens(i) is True]
    return res


print(filter(data=rand_list, evens=evens))

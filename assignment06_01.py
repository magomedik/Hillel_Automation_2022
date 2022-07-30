# зчитати ввод від користувача - речення (текст) - та порахувати кожне слово у реченні,
# кількість разів воно зустрічається у реченні. Також порахувати статистику використаних
# літер. Для зберігання статистик використати словники.
#
# Підказки:
# * input
# * str.split
# * for word in sequence
# * if key in dict
# * if key not in dict

import collections

text = input("Введіть якийсь текст: ")
list_words = text.split()
count_words = len(text.split())

stat_of_words = {item:list_words.count(item) for item in list_words}
stat_of_letter = dict(collections.Counter(text))

print(count_words)
print(stat_of_words)
print(stat_of_letter)


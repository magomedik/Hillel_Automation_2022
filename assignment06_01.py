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
print(len(list_words))

# variant 1

stat_of_words = dict(collections.Counter(list_words))
stat_of_letter = dict(collections.Counter(text))


print(stat_of_words)
print(stat_of_letter)

# variant 2 (manually, inconvenient and costly)

d_words = {word: list_words.count(word) for word in list_words}
d_letter = {letter: text.count(letter) for letter in text}

print(d_words)
print(d_letter)

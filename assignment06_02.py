# Є словник з ключами-строками та елементами-списками строк, наприклад:
#

data = {
'colors': ['red', 'green', 'blue', 'purple'],
'fruits': ['pineapple', 'orange', 'banana'],
'clothes': ['coat', 'tshirt']
}

# Завдання: перебудувати словник (не створюючи новий) таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника.
#
# Підказки:
# * dict[key] = value
# * for key in dict
# * for value in dict[key]



for k in tuple(data.keys()):
    v = data.pop(k)
    for x in v:
        data[x] = k

print(data)


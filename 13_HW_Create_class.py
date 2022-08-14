# Розробити клас Human.
# Людина має:
# Ім'я
# Прізвище
# Дату народження
# Стать
# Енергію = 100

# Люди можуть:
# Їсти (Енергія +5)
# Спати (Енергія +10)
# Говорити (Енергія -5)
# Ходити (Енергія -10)
# Робити домашку (Енергія -90)
#
# Створити 3 чоловіків та 2 жінок, Задати кожному з них виконання декількох дій,
# вивести в кого найбільше енергії лишилося.

from datetime import date
from operator import attrgetter

class Human:
    def __init__(self, name: str, surname: str, date_birth: date, sex: str):
        self.name = name
        self.surname = surname
        self.date_birth = date_birth
        self.sex = sex
        self.energy = 100

    def eat(self):
        self.energy += 5

    def sleep(self):
        self.energy += 10

    def speak(self):
        self.energy -= 5

    def walk(self):
        self.energy -= 10

    def do_hw(self):
        self.energy -= 90


man1 = Human("Liam", "Johnson", date(2000, 1, 1), "male")
man1.eat()
man1.do_hw()
man1.sleep()

man2 = Human("Alex", "Brenamer", date(1990, 1, 29), "male")
man2.sleep()
man2.speak()
man2.eat()

man3 = Human("John", "Doe", date(1988, 2, 28), "female")
man3.eat()
man3.speak()

woman1 = Human("Julia", "Henkok", date(1999, 12, 31), "female")
woman1.sleep()
woman1.eat()

woman2 = Human("Margo", "Smith", date(1982, 1, 7), "female")
woman2.walk()
woman2.speak()


l = [man1, man2, man3, woman1, woman2]
max_attr = max(l, key=attrgetter('energy'))
print(f"The maximum energy value of {max_attr.energy} belongs to {max_attr.name}")

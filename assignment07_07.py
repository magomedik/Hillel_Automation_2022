"""Задача: написати функцію сalculator для двух операндів .

   Деталі:
            * функція приймає три аргумента - лівий операнд, оператор, правий операнд
            * функція повинна повернути результат операції над операндами
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * calculate(2, "+", 2) -> повертає 4
            * calculate("hello world!", "*", 2) -> повертає "hello world!hello world!"
            * calculate(10, ")", 10) -> повертає None
"""


def calculate(x, operand, y):
    if operand == "+":
        print(x + y)
    elif operand == "-":
        print(x - y)
    elif operand == "*":
        print(x * y)
    elif operand == "/":
        print(x / y)
    else:
        print(None)

calculate(2, "+", 2)
calculate("hello world!", "*", 2)
calculate(10, ")", 10)
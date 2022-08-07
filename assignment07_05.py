"""Завдання: доповнити дефініції функцій (де тіло це pass інстркуція) для
             перерахунку шкал C(elsius) в F(ahrenheit)
             та у зворотньому напрямку.

   Hint: формули конвертації між C та F взяти в неті
"""

CELCISUS_SIGN = "C"
FAHRENHEIT_SIGN = "F"
QUIT = "q"
ALLOWED_INPUT = {CELCISUS_SIGN, FAHRENHEIT_SIGN, QUIT}


def convert_to_celsius(value):
    """Converts degrees value from fahrenheit celsius to."""
    return (value-32.0)*(5/9)


def convert_to_fahrengeit(value):
    """Converts degrees value from celsius to fahrenheit."""
    return (value*1.8)+32.0


def converter(value, target):
    """Converts value by using appropriate type of target converter."""

    if target == CELCISUS_SIGN:
        return convert_to_celsius(value)  # ретурн припиняє виконання функції
                                          # з будь якого рядка функції (не тільки у кінці)

    return convert_to_fahrengeit(value)


def select_conversion_type():
    """Accepts user selection as to conversion type."""

    while True:
        print("F) Convert to Fahrenheit")
        print("C) Convert to Celsium")
        try:
            selection = input("Enter selection (q - to exit): ")
        except Exception:
            continue

        if selection not in ALLOWED_INPUT:
            print(
                f"{selection} is not accepted (allowed: {sorted(ALLOWED_INPUT)}). "
                "Try again."
            )
            continue
        else:
            break

    return selection


def read_degrees():
    """Reads from user degrees value to be converted."""

    while True:
        try:
            degrees = float(input("Enter degrees value: "))
        except Exception:
            print("Input is invalid - only accpet numeric values. Try again.")
            continue
        else:
            break

    return degrees


def main():
    """Handles main workflow with the application."""

    while True:
        conversion_type = select_conversion_type()

        if conversion_type is None or conversion_type == QUIT:
            break

        to = conversion_type
        from_ = CELCISUS_SIGN if conversion_type == FAHRENHEIT_SIGN \
            else FAHRENHEIT_SIGN

        value = read_degrees()

        if value is None:
            print("Degrees value is invalid.")
            break

        result = converter(value, to)

        print(f"{value}{from_} is {result}{to}")


if __name__ == "__main__":
     main()


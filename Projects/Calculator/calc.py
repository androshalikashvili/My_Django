# შემოწმება რიცხვის შეყვანაზე
def chek_input_number(value):
    while True:
        try:
            value = float(input(value))
            return value
        except ValueError:
            print("Please input number!")


def check_operand(value):
    pass


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Don`t divide by zero"


# რიცხვის შეყვანა
number_1 = chek_input_number("Please input first number: ")
number_2 = chek_input_number("Please input second number: ")


# ქმედების არჩევის შემოწმება
while True:
    try:
        qmedeba = input("Please choose operation (+, -, *, /): ")

        if qmedeba in ['+', '-', '*', '/']:
            break
        else:
            print("Error: choose the rigth operation.")

    except KeyboardInterrupt as ex:
        print("\nProgramm closed by user (Ctrl+C)")
        break


# მოქმედების არჩევა
if qmedeba == '+':
    res = add(number_1, number_2)
elif qmedeba == '-':
    res = minus(number_1, number_2)
elif qmedeba == '*':
    res = multiply(number_1, number_2)
else:
    res = divide(number_1, number_2)

print(f"Result: {res}") # შედეგის გამოტანა

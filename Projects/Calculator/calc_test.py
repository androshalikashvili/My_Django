# Check for number input
def check_input_number(value):
    while True:
        try:
            value = float(input(value))
            return value
        except ValueError:
            print("Please input number!")


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


# recivie number
number_1 = check_input_number("Please input first number: ")
number_2 = check_input_number("Please input second number: ")


# Check action selection
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


#Action selection check
if qmedeba == '+':
    res = add(number_1, number_2)
elif qmedeba == '-':
    res = minus(number_1, number_2)
elif qmedeba == '*':
    res = multiply(number_1, number_2)
else:
    res = divide(number_1, number_2)

#produce results
print(f"Result: {res}")

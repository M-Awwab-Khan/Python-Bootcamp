import os
from art import logo
# Add


def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# Divide


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def start():
    print(logo)
    num1 = float(input("What's the first number? "))
    for operation in operations:
        print(operation)

    while True:

        operation = input("Pick an operation: ")
        num2 = float(input("What's the second number? "))
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        should_continue = input(
            f"Type 'y' to continue calculating with {result} or 'n' to start new calculation: ")
        if should_continue == 'y':
            num1 = result
        else:
            os.system('clear')
            start()


start()

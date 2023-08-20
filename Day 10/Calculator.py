
from art import calculatorLogo, calculator
print(f" {calculator}{calculatorLogo}")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


def calculate(num1, num2, choice):
    if choice == '+':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '-':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '/':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")


cont = True
while cont:

    num1 = float(input("Enter first number: "))
    print("Select operation:")
    print("+")
    print("-")
    print("*")
    print("/")
    choice = input("Enter choice: ")
    num2 = float(input("Enter second number: "))
    calculate(num1, num2, choice)
    temp = input("Wnat to calculate again? yes or no").lower()
    if (temp == "yes"):
        cont = True
    else:
        cont = False

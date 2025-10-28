def add (num1, num2):
    return num1 + num2
def subtract (num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2
def divide (num1, num2):
    return num1 / num2





while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /), enter 'q' to quit: ")
    if operator == '+':
        result = add(num1, num2)
        print(result)
    elif operator == '-':
        result = subtract(num1, num2)
        print(result)
    elif operator == '*':
        result = multiply(num1, num2)
        print(result)
    elif operator == '/':
        result = divide(num1, num2)
        print(result)
    elif operator == 'q':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid operator, please try again.")

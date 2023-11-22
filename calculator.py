#Write a program to create a Simple Calculator using a switch case and function for every operation.
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

def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    if choice in operations:
        result = operations[choice](num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice")

# Example usage:
calculator()
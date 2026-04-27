# Calculator program that performs basic arithmetic operations based on user input.
#-----------------Imports---------------
import math

#----------------Functions----------------
def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("'q' or 'quit' to exit")
    selection = int(input("Enter Selection:\n"))
    return selection
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

#----------------Main Program----------------
user_selection = menu()
while user_selection != "q" or user_selection != "quit":
    user_selection = menu()
    if user_selection < 1 or user_selection > 4:
        print("Error Dectected: Enter A Valid Selection.")
    elif user_selection == 1:
        x = float(input("Enter the First Number:\n"))
        y = float(input("Enter the Second Number:\n"))
        result = add(x, y)
    elif user_selection == 2:
        x = float(input("Enter the First Number:\n"))
        y = float(input("Enter the Second Number:\n"))
        result = subtract(x, y)
    elif user_selection == 3:
        x = float(input("Enter the First Number:\n"))
        y = float(input("Enter the Second Number:\n"))
        result = multiply(x, y)
    elif user_selection == 4:
        x = float(input("Enter the First Number:\n"))
        y = float(input("Enter the Second Number:\n"))
        result = divide(x, y)
#----------------Testing-Code----------------
print(f"User Selection: {user_selection}")
print(f"Result: {result}")
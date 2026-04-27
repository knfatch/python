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
    result = x + y
    return result
def subtract(x, y):
    result = x - y
    return result
def multiply(x, y):
    result = x * y
    return result
def divide(x, y):
    result = x / y
    return result
#---------------Variables--------------------


#----------------Main Program----------------
user_selection = menu()
while user_selection != "q" or user_selection != "quit":
    if user_selection < 1 or user_selection > 4:
        print("Error Dectected: Enter A Valid Selection.")
    elif user_selection == 1:  #Addition
        x = float(input("Enter the First Number: Add\n"))
        y = float(input("Enter the Second Number: Add\n"))
        result = add(x, y)
        print("-----------------------")
        print(f"Result: {result}")
        print("-----------------------")
    elif user_selection == 2:  #Subtraction
        x = float(input("Enter the First Number: Subtract\n"))
        y = float(input("Enter the Second Number: Subtract\n"))
        result = subtract(x, y)
        print("-----------------------")
        print(f"Result: {result}")
        print("-----------------------")
    elif user_selection == 3:  #Multiplication
        x = float(input("Enter the First Number: Multiply\n"))
        y = float(input("Enter the Second Number: Multiply\n"))
        result = multiply(x, y)
        print("-----------------------")
        print(f"Result: {result}")
        print("-----------------------")
    elif user_selection == 4:  #Division
        x = float(input("Enter the First Number: Divide\n"))
        y = float(input("Enter the Second Number (Can't Be '0'): Divide\n"))
        while y == 0:
            print(f"{x} cannot be divided by 0. Please enter a valid number.")
            y = float(input("Enter the Second Number: Divide\n"))
        result = divide(x, y)
        print("-----------------------")
        print(f"Result: {result}")
        print("-----------------------")
#----------------Testing-Code----------------
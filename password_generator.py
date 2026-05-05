# Program that creates a random password importing the random module.
#--------------Imports-------------------
import random

#-----------------Functions--------------
def set_pass_len():
    password_len = int(input("Enter a number for the length of the password (Minimun of 15):\n"))
    while password_len < 15:
        password_len = int(input("A minimun of 15 characters are requried. Please select a higher number.\n"))
    return password_len
def create_pass(length):
    password = ""

#---------------Variables----------------
low_letters = "abcdefghijklmnopqrstuvwxyz"
cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
char = "_-%$!?"

#---------------Main-Program-------------
print("Password Generator App")
password_len = set_pass_len()
# create_pass(password_len)               #Placeholder txt until function is complete

#---------------Testing-Code------------- "Ctrl + /" to comment selected txt
print(password_len)
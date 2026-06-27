## write a program to input two numbers and divide them. use exception handling to display a message when division by zero occurs.

n1 = int(input("enter 1st number"))
n2 = int(input("enter 2nd number"))
try:
    result = n1/n2
    print(result)
except:
    print("sorry not possible to divide by zero")

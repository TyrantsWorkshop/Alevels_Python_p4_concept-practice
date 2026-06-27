##write a iterative function find factorial of a number

def factorial(number):
   
    total = 1
    x = number
    for count in range(number,0,-1):
        total = total * count

    return (total)

number=int(input(" Enter a number"))
print("factorial of number:",factorial(number))

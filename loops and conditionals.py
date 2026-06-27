## write programs using loops and conditionals for the following:
## check if a number is positive, negative or zero, sum numbers 1 to 10, calculate factorial,
## countdown using while loop, assign grade from score, sum even numbers 2 to 20,
## password login with 3 attempts, print number pattern, check leap year.

num = int(input("enter a number"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

total = 0
for i in range(1, 11):
    total = total + i
print("sum 1 to 10:", total)

n = int(input("enter n"))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("factorial:", factorial)

count = 5
while count > 0:
    print(count)
    count = count - 1

score = int(input("enter score"))
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "F"
print("grade:", grade)

even_sum = 0
for i in range(2, 21, 2):
    even_sum = even_sum + i
print("sum of evens:", even_sum)

password = input("enter password")
attempts = 0
correct = "python123"
while attempts < 3:
    if password == correct:
        print("access granted")
        break
    attempts = attempts + 1
    password = input("try again: ")
else:
    print("access denied")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

year = int(input("enter year"))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("not leap year")

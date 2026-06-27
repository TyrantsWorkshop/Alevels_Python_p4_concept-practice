## write functions for the following tasks and call each one from the main program:
## greet a user by name, add two numbers, check if a number is even, find maximum in a list,
## calculate bill after discount, count vowels in a string, generate fibonacci sequence and print multiplication table.

def greet(name):
    print("Hello,", name)

greet("Student")

def add(a, b):
    return a + b

result = add(10, 25)
print("sum:", result)

def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(is_even(8))
print(is_even(7))

def find_max(arr):
    maximum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum

data = [3, 17, 9, 42, 8]
print("max:", find_max(data))

def calculate_bill(price, qty, discount):
    total = price * qty
    disc_amount = total * discount / 100
    return total - disc_amount

print("bill:", calculate_bill(1000, 3, 10))

def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1
    return count

print("vowels:", count_vowels("programming"))

def fibonacci(n):
    a = 0
    b = 1
    sequence = []
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(8))

def multiply_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

multiply_table(5)

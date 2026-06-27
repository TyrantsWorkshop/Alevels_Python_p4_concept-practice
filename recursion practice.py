## write recursive functions for the following:
## factorial, sum of digits, power, countdown, fibonacci sequence, reverse a string and gcd of two numbers.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("factorial of 5:", factorial(5))

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print("sum of digits:", sum_digits(12345))

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print("2^6:", power(2, 6))

def countdown(n):
    if n == 0:
        print("done")
        return
    print(n)
    countdown(n - 1)

countdown(5)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(10):
    print(fib(i), end=" ")
print()

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("gcd:", gcd(48, 18))

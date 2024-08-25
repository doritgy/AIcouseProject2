import random, statistics, math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b
def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

def is_prime(a):
    if a < 0:
        raise ValueError(' math domain error')
    if a == 1 or a <= 0:
        return False
    for i in range(2, a):
        print(i)
        if a % i == 0:
            return False
    else: return True

def factorial(a):
    if a == 0 or a == 1:
        return 1
    if a < 0:
        raise ValueError("factorial not defined for negative values")
    return math.factorial(a)
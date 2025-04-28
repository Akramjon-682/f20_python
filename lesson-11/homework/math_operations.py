# math_operations.py
import math_operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0 ga bo‘lib bo‘lmaydi!"
    return a / b

print(math_operations.add(2, 3))
print(math_operations.subtract(5, 2))

# Homework Solutions

# 1. Modify String with Underscores
def modify_string_with_underscores(txt):
    result = ""
    i = 0
    count = 0
    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3:
            if txt[i] in 'aeiou' or (i + 1 < len(txt) and txt[i+1] == '_'):
                j = i + 1
                while j < len(txt):
                    if txt[j] not in 'aeiou' and txt[j] != '_':
                        result += '_'
                        count = 0
                        break
                    result += txt[j]
                    i = j
                    j += 1
            else:
                if i != len(txt) - 1:
                    result += '_'
                count = 0
        i += 1
    return result

# 2. Integer Squares
def print_integer_squares(n):
    for i in range(n):
        print(i ** 2)

# 3. Loop-Based Exercises

def exercise1():
    i = 1
    while i <= 10:
        print(i)
        i += 1

def exercise2():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

def exercise3(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print("Sum is:", total)

def exercise4(n):
    for i in range(1, 11):
        print(n * i)

def exercise5(numbers):
    for num in numbers:
        if num > 500:
            break
        if num > 150:
            continue
        if num % 5 == 0:
            print(num)

def exercise6(number):
    print("Total digits:", len(str(number)))

def exercise7():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()

def exercise8(lst):
    for item in reversed(lst):
        print(item)

def exercise9():
    for i in range(-10, 0):
        print(i)

def exercise10():
    for i in range(5):
        print(i)
    print("Done!")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def exercise11():
    print("Prime numbers between 25 and 50:")
    for i in range(25, 51):
        if is_prime(i):
            print(i)

def exercise12():
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(10):
        print(a, end='  ')
        a, b = b, a + b
    print()

def exercise13(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print(f"{n}! = {result}")

# 4. Return Uncommon Elements of Lists
def return_uncommon_elements(list1, list2):
    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    for k in c1:
        if k not in c2:
            result.extend([k]*c1[k])
        elif c1[k] > c2[k]:
            result.extend([k]*(c1[k]-c2[k]))
    for k in c2:
        if k not in c1:
            result.extend([k]*c2[k])
        elif c2[k] > c1[k]:
            result.extend([k]*(c2[k]-c1[k]))
    return result

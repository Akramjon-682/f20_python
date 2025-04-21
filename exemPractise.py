
# # 31. Create file with alphabet letters and N per line
# n = 13
# with open("alphabet.txt", "w") as f:
#     for i in range(0, 26, n):
#         f.write(" ".join(string.ascii_uppercase[i:i+n]) + "\n")

# # 29. Extract characters from multiple files into a list
# chars = []
# for filename in ["sample.txt", "list.txt"]:
#     with open(filename) as f:
#         chars.extend(list(f.read()))
# print(chars)

# 26. Check if a file is closed or not
# f = open("sample.txt")
# print("Closed?", f.closed)
# f.close()
# print("Closed?", f.closed)

# # 18. Find the longest word(s) in a file
# with open("sample.txt", "r") as f:
#     words = f.read().split()
#     longest = max(words, key=len)
#     print("Longest word:", longest)

# # 8. Handle ArithmeticError during division
# try:
#     result = 10 / 0
# except ArithmeticError as e:
#     print("Arithmetic error:", e)

# # 9. Handle UnicodeDecodeError when reading file with encoding issues
# try:
#     with open("text.txt", encoding="ascii") as f:
#         print(f.read())
# except UnicodeDecodeError:
#     print("Encoding issue while reading file.")

# # 10. Handle AttributeError in list operation
# try:
#     my_list = [1, 2, 3]
#     my_list.upper()
# except AttributeError:
#     print("List has no attribute 'upper'.")

# 2. digit_sum(k) funksiyasi
# # k sonining raqamlari yig'indisini hisoblaydi.
# def digit_sum(k):
#     return sum(int(digit) for digit in str(k))

# # Test:
# print("\n2. digit_sum:")
# print(digit_sum(24))   # 6

# 1. is_prime(n) funksiyasi
# n soni tub bo‘lsa True, aks holda False qaytarsin.
# m = int(input(' funksiyasiga son kiriting : '))
# def isprime(n):
#     if n <=1 :
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# # Test:
# print("1. is_prime:")

# print(isprime(m))  # True

# # 9. Stack with Display
# class StackWithDisplay:
#     def __init__(self):
#         self.stack = []

#     def push(self, item): self.stack.append(item)
#     def pop(self): return self.stack.pop() if self.stack else "Empty"
#     def display(self): print(self.stack)



# # # 11. Bank Class
# class Bank:
#     def __init__(self):
#         self._accounts = {}  # protected attribute

#     def create_account(self, name, balance=0):
#         if name not in self._accounts:
#             if balance >= 0:
#                 self._accounts[name] = balance
#                 print(f"Account created for {name} with balance {balance}")
#             else:
#                 print("Initial balance cannot be negative.")
#         else:
#             print("Account already exists!")

#     def deposit(self, name, amount):
#         if amount <= 0:
#             print("Deposit amount must be positive.")
#             return
#         if name in self._accounts:
#             self._accounts[name] += amount
#             print(f"{amount} deposited to {name}. New balance: {self._accounts[name]}")
#         else:
#             print("Account not found.")

#     def withdraw(self, name, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be positive.")
#             return
#         if name in self._accounts:
#             if self._accounts[name] >= amount:
#                 self._accounts[name] -= amount
#                 print(f"{amount} withdrawn from {name}. New balance: {self._accounts[name]}")
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Account not found.")

#     def get_balance(self, name):
#         if name in self._accounts:
#             return f"Balance for {name}: {self._accounts[name]}"
#         else:
#             return "Account not found."

# b = Bank()

# b.create_account("Ali", 100)
# b.create_account("Vali")

# b.deposit("Ali", 50)
# b.withdraw("Ali", 30)
# print(b.get_balance("Ali"))  # Balance for Ali: 120

# b.withdraw("Vali", 10)       # Insufficient balance
# print(b.get_balance("Vali")) # Balance for Vali: 0

# b.deposit("Vali", -20)       # Xatolik
# b.withdraw("Ali", 1000)      # Insufficient balance

# 4. Shape and Subclasses
# import math

# # Umumiy shakl klassi (shablon)
# class Shape:
#     def area(self):
#         raise NotImplementedError("Area method must be implemented in subclass")

#     def perimeter(self):
#         raise NotImplementedError("Perimeter method must be implemented in subclass")

# # Aylana shakli
# class CircleShape(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# # Uchburchak shakli
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def perimeter(self):
#         return self.a + self.b + self.c

#     def area(self):
#         s = self.perimeter() / 2
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# # Kvadrat shakli
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

#     def perimeter(self):
#         return 4 * self.side
    

# circle = CircleShape(5)
# triangle = Triangle(3, 4, 5)
# square = Square(6)

# print("Circle area:", round(circle.area(), 2))
# print("Circle perimeter:", round(circle.perimeter(), 2))

# print("Triangle area:", round(triangle.area(), 2))
# print("Triangle perimeter:", triangle.perimeter())

# print("Square area:", square.area())
# print("Square perimeter:", square.perimeter())
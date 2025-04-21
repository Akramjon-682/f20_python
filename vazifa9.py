import math
from datetime import datetime



# # 1. Circle Class
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# c = Circle(7)
# print("Radius:", c.radius)
# print("Area:", c.area())
# print("Perimeter:", c.perimeter())  

# # 2. Person Class
# class Person:
#     def __init__(self, name, country, birthdate):
#         self.name = name
#         self.country = country
#         self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

#     def get_name(self):
#         return self.name    

#     def age(self):
#         today = datetime.today()
#         return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
# p = Person("Ali","Amerika","1997-08-12")
# print("my age is:", p.age())
# print("my name is", p.get_name())


# # 3. Calculator Class
# class Calculator:
#     def add(self, a, b): return a + b
#     def subtract(self, a, b): return a - b
#     def multiply(self, a, b): return a * b
#     def divide(self, a, b): return a / b if b != 0 else "Division by zero"

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

# # 5. Binary Search Tree Class
# from graphviz import Digraph

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, root, key):
#         if root is None:
#             return Node(key)
#         if key < root.val:
#             root.left = self.insert(root.left, key)
#         else:
#             root.right = self.insert(root.right, key)
#         return root

#     def search(self, root, key):
#         if root is None or root.val == key:
#             return root
#         if key < root.val:
#             return self.search(root.left, key)
#         return self.search(root.right, key)

#     # Add the draw_tree method
#     def draw_tree(self, root):
#         dot = Digraph()

#         def add_nodes_edges(node):
#             if node:
#                 dot.node(str(node.val))
#                 if node.left:
#                     dot.edge(str(node.val), str(node.left.val))
#                     add_nodes_edges(node.left)
#                 if node.right:
#                     dot.edge(str(node.val), str(node.right.val))
#                     add_nodes_edges(node.right)

#         add_nodes_edges(root)
#         dot.render('tree', view=True)  # Will open the tree in the default viewer

# bst = BST()
# root = None

# # Add nodes
# for key in [50, 30, 70, 20, 40, 60, 80]:
#     root = bst.insert(root, key)

# # Draw the tree
# bst.draw_tree(root)

# # Search for a node
# found = bst.search(root, 40)
# print("Found:", found.val if found else "Not Found")



# # 6. Stack Data Structure
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         return self.stack.pop() if self.stack else "Stack is empty"

#     def __str__(self):
#         return str(self.stack)  # Returns a string representation of the stack

# # Usage
# c = Stack()
# c.push(10)
# c.push(20)
# c.push(30)

# print(c)  # This will print the contents of the stack: [10, 20, 30]

# 7. Linked List Data Structure
# class NodeLL:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=' -> ')
#             temp = temp.next
#         print("None")

#     def insert(self, data):
#         new_node = NodeLL(data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete(self, key):
#         temp = self.head
#         if temp is not None and temp.data == key:
#             self.head = temp.next
#             return
#         prev = None
#         while temp is not None and temp.data != key:
#             prev = temp
#             temp = temp.next
#         if temp is None:
#             return
#         prev.next = temp.next

# # 8. Shopping Cart Class
# class ShoppingCart:
#     def __init__(self):
#         self.items = {}

#     def add_item(self, name, price):
#         self.items[name] = price

#     def remove_item(self, name):
#         if name in self.items:
#             del self.items[name]

#     def total_price(self):
#         return sum(self.items.values())

# # 9. Stack with Display
# class StackWithDisplay:
#     def __init__(self):
#         self.stack = []

#     def push(self, item): self.stack.append(item)
#     def pop(self): return self.stack.pop() if self.stack else "Empty"
#     def display(self): print(self.stack)

# # 10. Queue Data Structure
# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, item): self.queue.append(item)
#     def dequeue(self): return self.queue.pop(0) if self.queue else "Empty"
# C = Queue()
# C.enqueue(2)
# C.enqueue(5)
# print("Queue:", C.queue)     # [2, 5]


# 11. Bank Class
class Bank:
    def __init__(self):
        self._accounts = {}  # protected attribute

    def create_account(self, name, balance=0):
        if name not in self._accounts:
            if balance >= 0:
                self._accounts[name] = balance
                print(f"Account created for {name} with balance {balance}")
            else:
                print("Initial balance cannot be negative.")
        else:
            print("Account already exists!")

    def deposite(self, name, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        if name in self._accounts:
            self._accounts[name] += amount
            print(f"{amount} deposited to {name}. New balance: {self._accounts[name]}")
        else:
            print("Account not found.")

    def withdraw(self, name, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if name in self._accounts:
            if self._accounts[name] >= amount:
                self._accounts[name] -= amount
                print(f"{amount} withdrawn from {name}. New balance: {self._accounts[name]}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def get_balance(self, name):
        if name in self._accounts:
            return f"Balance for {name}: {self._accounts[name]}"
        else:
            return "Account not found."







b = Bank()

b.create_account("Ali", 100)
b.create_account("Vali")

b.deposite("Ali", 50)
b.withdraw("Ali", 30)
print(b.get_balance("Ali"))  # Balance for Ali: 120

b.withdraw("Vali", 10)       # Insufficient balance
print(b.get_balance("Vali")) # Balance for Vali: 0

b.deposite("Vali", -20)       # Xatolik
b.withdraw("Ali", 1000)      # Insufficient balance



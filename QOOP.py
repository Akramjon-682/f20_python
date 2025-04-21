# # 1
# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} is barking!")

# dog1 = Dog("Rex", "Bulldog")
# dog1.bark()

# # 2
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start_engine(self):
#         print(f"The engine of {self.brand} {self.model} is starting.")

# my_car = Car("Toyota", "Corolla")
# my_car.start_engine()

# # 3
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def read(self):
#         print(f"Reading {self.title} by {self.author}")

# book1 = Book("1984", "George Orwell")
# book1.read()

# # 4
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# person1 = Person("Alice", 30)
# person1.introduce()

# # 5
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def study(self):
#         print(f"{self.name} is studying.")

# student1 = Student("John", "A")
# student1.study()

# # 6
# class Animal:
#     def __init__(self, species):
#         self.species = species

#     def make_sound(self):
#         print(f"{self.species} makes a sound.")

# cat = Animal("Cat")
# cat.make_sound()

# # 7
# class Phone:
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price

#     def show_info(self):
#         print(f"Phone model: {self.model}, Price: ${self.price}")

# phone1 = Phone("iPhone", 999)
# phone1.show_info()

# # 8
# class Movie:
#     def __init__(self, title, year):
#         self.title = title
#         self.year = year

#     def show_movie_info(self):
#         print(f"{self.title} ({self.year})")

# movie1 = Movie("Inception", 2010)
# movie1.show_movie_info()

# # 9
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited ${amount}. New balance: ${self.balance}")

# account1 = BankAccount(500)
# account1.deposit(100)

# # 10
# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def display_color(self):
#         print(f"The color of the shape is {self.color}.")

# shape1 = Shape("red")
# shape1.display_color()

# # 1
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# account1 = BankAccount(1000)
# account1.deposit(500)
# print(account1.get_balance())  # 1500

# # 2
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def set_name(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

# person1 = Person("Alice", 30)
# person1.set_name("Bob")
# print(person1.get_name())  # Bob

# # 3
# class Car:
#     def __init__(self, make, model):
#         self.__make = make
#         self.__model = model

#     def set_make(self, make):
#         self.__make = make

#     def get_make(self):
#         return self.__make

# car1 = Car("Toyota", "Corolla")
# car1.set_make("Honda")
# print(car1.get_make())  # Honda

# # 4
# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary

# employee1 = Employee("John", 50000)
# print(employee1.get_salary())  # 50000

# # 5
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width

#     def set_length(self, length):
#         self.__length = length

#     def set_width(self, width):
#         self.__width = width

#     def get_area(self):
#         return self.__length * self.__width

# rectangle1 = Rectangle(10, 5)
# print(rectangle1.get_area())  # 50

# # 6
# class Product:
#     def __init__(self, name, price):
#         self.__name = name
#         self.__price = price

#     def apply_discount(self, discount):
#         self.__price = self.__price * (1 - discount)

#     def get_price(self):
#         return self.__price

# product1 = Product("Shoes", 100)
# product1.apply_discount(0.2)
# print(product1.get_price())  # 80

# # 7
# class Customer:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def set_age(self, age):
#         if age >= 18:
#             self.__age = age

#     def get_age(self):
#         return self.__age

# customer1 = Customer("Alice", 30)
# customer1.set_age(25)
# print(customer1.get_age())  # 25

# # 8
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.__balance

# account1 = BankAccount(1000)
# account1.withdraw(500)
# print(account1.get_balance())  # 500

# # 9
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def birthday(self):
#         self.__age += 1

#     def get_age(self):
#         return self.__age

# person1 = Person("Bob", 25)
# person1.birthday()
# print(person1.get_age())  # 26

# # 10
# class Student:
#     def __init__(self, name, marks):
#         self.__name = name
#         self.__marks = marks

#     def update_marks(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks

# student1 = Student("John", 80)
# student1.update_marks(90)
# print(student1.get_marks())  # 90


# # 1
# class Animal:
#     def speak(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# dog = Dog()
# dog.speak()  # Dog barks

# # 2
# class Shape:
#     def area(self):
#         return 0

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# circle = Circle(5)
# print(circle.area())  # 78.5

# # 3
# class Vehicle:
#     def start(self):
#         print("Starting vehicle")

# class Car(Vehicle):
#     def start(self):
#         print("Starting car")

# car = Car()
# car.start()  # Starting car

# # 4
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

# manager = Manager("Alice", 50000, "HR")
# print(manager.name)  # Alice
# print(manager.department)  # HR

# # 5
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self.grade = grade

# student = Student("Bob", 20, "A")
# print(student.name)  # Bob
# print(student.grade)  # A

# # 6-
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

# class Motorcycle(Vehicle):
#     def __init__(self, brand, type):
#         super().__init__(brand)
#         self.type = type

# motorcycle = Motorcycle("Yamaha", "Sport")
# print(motorcycle.brand)  # Yamaha
# print(motorcycle.type)  # Sport


# ✅ super() nima qiladi?
# super() — bu ota (parent) klassning metodlariga, funksiyalariga yoki atributlariga kirish imkonini beradi.
# Bu degani: super() orqali ota klassdagi istalgan metod, atribut, funksiya yoki hatto propertyga ham murojaat qilsa bo‘ladi.

# 🔸 super() dan keyin nima chaqirsa bo‘ladi?
# Chaqiriladigan narsa	Misol	Izoh
# Metod	super().greet()	Eng keng tarqalgan holat.
# Constructor (__init__)	super().__init__(name)	Ota klassning konstruktorini chaqirish.
# Atribut	super().color	Agar ota klassda self.color bo‘lsa.
# Property (xususiyat)	super().area	Property orqali hisoblangan qiymat.
# Method chaining	super().method().another_method()	Metod natijasi obyekt bo‘lsa.
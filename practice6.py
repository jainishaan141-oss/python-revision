# Activity 1 — Employee Class
# Create an Employee class with:
# Name
# ID
# Salary
# Create two objects and display their information.

# class Employee:
#     def __init__(self, name, id, salary):
#         self.name = name
#         self.id = id
#         self.salary = salary
#     def display(self):
#         print("name :", self.name)
#         print("id :", self.id)
#         print("salary :", self.salary)
# e1 = Employee("ishaan", 12, 111111)
# e2 = Employee("bob", 5, 2222222)
# e1.display()
# e2.display()    


# Activity 2 — Rectangle Class
# Create a Rectangle class with:
# Length
# Width
# Create a method area() to calculate the area.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def display(self):
#         print(self.length * self.width)
# rec = Rectangle(10, 10)
# rec.display()


# Activity 3 — Bank Account
# Create a BankAccount class with:
# Account holder name
# Balancence)


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposite(self, amount):
#         self.balance += amount
#         print(self.balance)
#     #     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(self.balance)
#         else:
#             print("insuficient balance")
# s1 = BankAccount("ishaan", 200000)
# s1.deposite(5000)
# s1.withdraw(3000)
# Create methods:
# deposit()
# withdraw()


# 4. Write a Python class named Rectangle that takes width and height as attributes and has a method named calculate_area().

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def calculate_area(self):
#         return self.width * self.height
# rect = Rectangle(5, 10)
# print("The area of the rectangle is:", rect.calculate_area())


# 5. Create a class called Employee with attributes name and salary. Add a method give_raise(amount) that increases the salary by that amount

# class Employee:
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary
#     def give_raise(self, amount: float):
#         self.salary += amount
# emp = Employee("Alice", 50000.0)
# emp.give_raise(5000.0)
# print(emp.salary) 

# 6. Look at this expression: car1 = Car("Red"). Is car1 a class or an object? Explain your answer.

# class Car:
#     def __init__(self, color):
#         self.color = color 
# car1 = Car("Red")
# print(car1.color)


# 8. Write a Python class named Playlist that stores a list of song titles as an attribute and includes a method add_song(title) to expand the list.

# class Playlist:
#     def __init__(self):
#         self.songs = []
#     def add_song(self, title):
#         self.songs.append(title)
# my_playlist = Playlist()
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Hotel California")
# my_playlist.add_song("Stayin' Alive")
# print(my_playlist.songs)


# 10. Debugging Challenge: The code snippet below fails to execute correctly. Locate the programmatic bug, explain the issue, and provide a functional correction.

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#     def multiply(self):
#         return self.num1 * self.num2
# calc = Calculator(4,5)
# print(calc.multiply())


# 1. Create a `Student` class with:
# - Name
# - Age
# - Course
# Create two objects and display their information.

# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def display(self):
#         print("name:", self.name)
#         print("age:", self.age)
#         print("course:", self.course)
# s1 = Student("ishaan", 17, "python")
# s1.display()
# s2 = Student("bob", 18, "python")
# s2.display()
# s3 = Student("john", 19, "python")
# s3.display()


# 2. Create a `Book` class with:
# - Title
# - Author
# - Price
# Create a method `display()`.

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def display(self):
#         print("title:", self.title)
#         print("author:", self.author)
#         print("price:", self.price)
# s1 = Book("rich dad poor dad", "ishaan", 170)
# s1.display()
# s2 = Book("atomic habits", "bob", 200)
# s2.display()
# s3= Book("chankya nitti", "john", 250)
# s3.display()






# Part 2: OOP — 15 Coding Questions
# These questions cover classes, objects, constructors, instance methods, encapsulation, inheritance, abstraction and polymorphism.

# Level 1 — Classes, Objects and Constructors

# 31. Student class
# Create a Student class with name and marks attributes. Add a method to display the student's details.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def display(self):
#         print(self.name)
#         print(self.marks)
# student1 = Student("bob", 90)
# student1.display()

# 32. Rectangle calculator
# Create a Rectangle class with length and width. Implement methods to calculate area and perimeter.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def display(self):
#         print("area:", self.width * self.length)
#         print("perimeter:", 2 * self.width + self.length)
# s1 = Rectangle(5, 5)
# s2 = Rectangle(2, 2)
# s1.display()
# s2.display()

# 33. Bank account
# Create a `BankAccount` class with an account holder's name and balance. 
# Implement `deposit()` and `withdraw()` methods. Reject withdrawals exceeding the available balance.

# class BankAccount:
#   def __init__(self, account_holder, balance = 0):
#     self.account_holder = account_holder
#     self.balance = balance
#   def deposit(self, amount):
#     if amount > 0:
#       self.balance += amount
#       print(f"New balance: ${self.balance}")
#     else:
#       print("Deposit amount must be positive.")
#   def withdraw(self, amount):
#     if amount <= 0:
#       print("Withdrawal amount must be positive.")
#     else:
#       self.balance -= amount
#       print(f"New balance: ${self.balance}")
# account = BankAccount("Alice", 500)
# account.deposit(200)
# account.withdraw(100)

# 34. Employee salary
# Create an `Employee` class with name and salary. 
# Add a method that calculates a 10% salary increase and displays the updated salary.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def increse_salary(self):
#         self.salary += self.salary * 10 / 100
#         print(self.name, self.salary)
# emp = Employee("bob", 20000)
# emp.increse_salary()

# 35. Product inventory
# Create a `Product` class with name, price and stock. 
# Implement methods to sell a quantity and restock the product, rejecting invalid quantities.

# class Product:
#     def __init__(self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock
#     def sell(self, quantity):
#         if quantity <= 0:
#             print("invalid quantity")
#         else:
#             self.stock -= quantity
#             print(self.stock)
#     def restock(self, quantity):
#         if quantity <= 0:
#             print("invalid quantity")
#         else:
#             self.stock += quantity
#             print(self.stock)
# p1 = Product("laptop", 10000, 25)
# p1.sell(15)
# p1.restock(20)

# Level 2 — Encapsulation, Inheritance and Polymorphism

# 36. Encapsulated bank account
# Create a BankAccount class with a private balance attribute. 
# Provide methods to deposit, withdraw and view the balance. Prevent negative deposits and invalid withdrawals.

# class BankAccount:
#     def __init__(self, balance = 0):
#         self.__balance = balance
#     def deposit(self, amount):
#         if amount <= 0:
#             print("invalid deposite")
#         else:
#             self.__balance += amount
#             print(amount)
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("invalid withdrawl")
#         elif amount > self.__balance:
#             print("insufficient funds")
#         else:
#             self.__balance -= amount
#             print(amount)
#     def check_balance(self):
#         return self.__balance
# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(400)
# print(account.check_balance())

#  37. Inheritance with employees
# Create a base class Employee and child classes Developer and Manager. 
# Give each child class an appropriate method to describe its work.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print(self.name, self.salary)
# class Developer(Employee):
#     def work(self):
#         print(self.name, "writes code and fixes bugs")
# class Manager(Employee):
#     def work(self):
#         print(self.name, "manages team and plans projects")
# dev = Developer("bob", 25000)
# dev.display()
# dev.work()
# mgr = Manager("john", 50000)
# mgr.display()
# mgr.work()

# 38. Method overriding
# Create a base class Animal with a sound() method. 
# Override it in Dog, Cat and Cow. Call the method on objects of all three classes.

# class Animal:
#     def sound(self):
#         print("some animal sound")
# class Dog(Animal):
#     def sound(self):
#         print("dog is barking")
# class Cat(Animal):
#     def sound(self):
#         print("cat meow")
# class Cow(Animal):
#     def sound(self):
#         print("cow moos")
# dog = Dog()
# cat = Cat()
# cow = Cow()
# dog.sound()
# cat.sound()
# cow.sound()

# 39. Polymorphic payment system
# Create CardPayment, UPIPayment and PayPalPayment classes. 
# Each should implement pay(amount). Write a loop that processes different payment objects through the same method interface.

# class CardPayment:
#     def pay(self, amount):
#         print("paid", amount, "using card")
# class UPIPayment:
#     def pay(self, amount):
#         print("paid", amount, "using UPI")
# class PayPalPayment:
#     def pay(self, amount):
#         print("paid", amount, "using PayPal")
# for pay in (CardPayment(), UPIPayment(), PayPalPayment()):
#     pay.pay(50500505050050)

# 40. Abstract class
# Use Python's abc module to create an abstract class Shape with an abstract area() method.Implement Circle and Rectangle subclasses.

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         print("circle area:", 3.14 * self.radius ** 2)
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         print("rectangle area:", self.length * self.width)
# c = Circle(5)
# r = Rectangle(5, 5)
# c.area()
# r.area()



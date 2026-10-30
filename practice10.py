# 1. Create a `BankAccount` class with a private:
# __balance
# Create a `get_balance()` method.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
# my_account = BankAccount(500)
# print(my_account.get_balance())

# 2. Create a `Student` class with private marks. Create:
# get_marks()
# set_marks()
# Only allow marks from 0 to 100.

# class Student:
#     def __init__(self, marks):
#         self.set_marks(marks)
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self, marks):
#         if 0 <= marks <= marks:
#             self.__marks = marks
#         else:
#             print("marks don't between 1 to 100")
# s1 = Student(90)
# print(s1.get_marks())
# s1.set_marks(100)
# print(s1.get_marks())
    
# 3. Animals
# Create:
# Animal
# Dog, Cat, Cow
# Each class should have:
# speak()

# class Animal:
#     def speak(self):
#         print("all animals are good")
# class Dog(Animal):
#     def speak(self):
#         print("dog is barking")
# class Cat(Animal):
#     def speak(self):
#         print("cow is meow")
# class Cow(Animal):
#     def speak(self):
#         print("cow is moos")
# animals = [Dog(), Cat(), Cow()]
# for i in animals:
#     i.speak()

# 4. Vehicles
# Create:
# Car, Bike, Boat
# Each class should have:
# move()

# class Car:
#     def move(self):
#         print("car speed is 20kmph")
# class Bike:
#     def move(self):
#         print("bike speed is 10kmph")
# class Boat:
#     def move(self):
#         print("boat speed is 5kmph")
# vehicles = [Car(), Bike(), Boat()]
# for i in vehicles:
#     i.move()

# 5. Create `Dog` and `Cat` classes.
# Both should contain:
# speak()
# Make them produce different outputs.

# class Dog:
#     def speak(self):
#         print("dog is barking")
# class Cat:
#     def speak(self):
#         print("cat is meow")
# animals = [Dog(), Cat()]
# for i in animals:
#     i.speak()

# 6. Create:
# Developer, Tester, Designer
# Each class should have:
# work()
# Display their different work using polymorphism.

# class Developer:
#     def work(self):
#         print("clear code and fixing bugs")
# class Tester:
#     def work(self):
#         print("test cases and ensuring quality")
# class Designer:
#     def work(self):
#         print("user interfaces and wireframes")
# coding = [Developer(), Tester(), Designer()]
# for i in coding:
#     i.work()


# 7. Create a payment system containing:
# UPI
# CreditCard
# PayPal
# Each should implement:
# pay(amount)
# Use one loop to process all payments.

# class PaymentMethod():
#     def pay(self, amount):
#         self.amount = amount
# class UPI(PaymentMethod):
#     def pay(self, amount):
#         print(f"paid ${amount :} using UPI")
# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         print(f"paid ${amount :} using CreditCard")
# class PayPal(PaymentMethod):
#     def pay(self, amount):
#         print(f"paid ${amount :} using PayPal")
# payment = [
#     (UPI(), 200),
#     (CreditCard(), 201),
#     (PayPal(), 202)
# ]
# for method, amount in payment:
#     method.pay(amount)






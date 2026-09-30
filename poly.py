# Activity 1 — Animals

# Create:

# ```
# Animal
# Dog
# Cat
# Cow
# ```

# Each class should have:

# ```
# speak()

# class Animal:
#     def speak(self):
#         print("animals are so good")
# class Dog(Animal):
#     def speak(self):
#         print("dog is barking")
# class Cat(Animal):
#     def speak(self):
#         print("cat is meow")
# class Cow(Animal):
#     def speak(self):
#         print("cow is moos")
# animals = [Dog(), Cat(), Cow()]
# for i in animals:
#     i.speak()

# Activity 2 — Vehicles

# Create:

# ```
# Car
# Bike
# Boat
# ```

# Each class should have:

# ```
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
# vehicle = [Car(), Bike(), Boat()]
# for i in vehicle:
#     i.move()

# Activity 1 — Animals
# Create:
# Animal
# Dog
# Cat
# Cow
# Each class should have:
# speak()

# class Animal:
#     def speak(self):
#         print("animals are so good")
# class Dog(Animal):
#     def speak(self):
#         print("dog is barking")
# class Cat(Animal):
#     def speak(self):
#         print("cat is meow")
# class Cow(Animal):
#     def speak(self):
#         print("cow is moos")
# animals = [Dog(), Cat(), Cow()]
# for i in animals:
#     i.speak()

# Activity 2 — Vehicles
# Create:
# Car
# Bike
# Boat
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
# vehicle = [Car(), Bike(), Boat()]
# for i in vehicle:
#     i.move()




# Create `Dog` and `Cat` classes.
# Both should contain:
# speak()
# Make them produce different outputs.

# class Cat:
#     def speak(self):
#         print("cat meows")
# class Dog:
#     def speak(self):
#         print("dog barks")
# animal = [Cat(), Dog()]
# for i in animal:
#     i.speak()

# Create a parent class `Animal` with:
# speak()
# Create `Dog` and `Cat` classes that override `speak()`.

# class Animal:
#     def speak(self):
#         print("many animals in world")
# class Dog(Animal):
#     def speak(self):
#         print("dog is barking")
# class Cat(Animal):
#     def speak(self):
#         print("cat is meow")
# animal = [Cat(), Dog()]
# for i in animal:
#     i.speak()

# Create three classes:
# Car
# Bike
# Bus
# Each should have a:
# move()
# method.
# Store their objects in a list and use a loop to call `move()`.

# class Car():
#     def move(self):
#         print("car speed is 20kmph")
# class Bike():
#     def move(self):
#         print("bike speed is 15kmph")
# class Bus():
#     def move(self):
#         print("bus speed is 10kmph")
# vehicle = [Car(), Bike(), Bus()]
# for i in vehicle:
#     i.move()

# Create:
# Developer
# Tester
# Designer
# Each class should have:
# work()
# Display their different work using polymorphism.

# class Developer():
#     def work(self):
#         print("clear code and fixing bugs")
# class Tester():
#     def work(self):
#         print("test cases and ensuring quality")
# class Designer():
#     def work(self):
#         print("user interfaces andwireframes")
# coding = [Developer(), Tester(), Designer()]
# for i in coding:
#     i.work()

# Create a payment system containing:
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
#         print(f"paid ${amount:.2f} using UPI.")
# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         print(f"paid ${amount:.2f} using CreditCard.")
# class PayPal(PaymentMethod):
#     def pay(self, amount):
#         print(f"paid ${amount:.2f} using PayPal.")
# payment = [
#     (UPI(), 200),
#     (CreditCard(), 201),
#     (PayPal(), 202)
# ]
# for  method, amount in payment:
#     method.pay(amount)

# Create a `Point` class and overload `+` so that:
# p1+p2
# adds their `x` and `y` coordinates.
# For example:
# p1 = (2, 3)
# p2 = (4, 5)
# Result = (6, 8)

# Create a parent class:
# Employee
# with:
# work()
# Create:
# Developer
# Tester
# Manager
# that override `work().
# Then create an employee list and demonstrate polymorphism.

# class Employee():
#     def work(self):
#         print("developer, tester, and designer thry all are empoyee")
# class Developer(Employee):
#     def work(self):
#         print("clear code and fixing bugs")
# class Tester(Employee):
#     def work(self):
#         print("test cases and ensuring quality")
# class Designer(Employee):
#     def work(self):
#         print("user interfaces andwireframes")
# coding = [Developer(), Tester(), Designer()]
# for i in coding:
#     i.work()
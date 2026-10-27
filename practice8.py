# 1. Create an Employee parent class and Developer child class. Add a programming language to Developer.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)
#         self.programming_language = programming_language
# dev = Developer("bob", 1111111, "Python")
# print(dev.name, dev.salary, dev.programming_language)

# 2. Create an Animal class with sound(). Override it in Dog and Cat.

# class Animal:
#     def sound(self):
#         print("some generic sound")
# class Dog(Animal):
#     def sound(self):
#         print("dog is barking")
# class Cat(Animal):
#     def sound(self):
#         print("cat is meow")
# dog = Dog()
# cat = Cat()
# print(dog.sound())
# print(cat.sound())


# 3. Create:
# Shape -- Circle Rectangle
# Give each class an appropriate `area()` method.

# pi = 3.14
# class Shape:
#     def area(self):
#         print("subclass must implement this method")
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         print(pi * (self.radius ** 2))
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         print(self.width * self.height)
# circle = Circle(5)
# rec = Rectangle(5, 5)
# print(circle.area(), rec.area())

# 4.
# Employee
#   ↓
# Developer
#   ↓
# Manager
# Use multilevel inheritance.
# Each level should have at least one attribute or method.

# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary
#     def display(self):
#         print("name :", self.name)
#         print("emp_id :", self.emp_id)
#         print("salary :", self.salary)
# class Developer(Employee):
#     def __init__(self, name, emp_id, salary, language):
#         super().__init__(name, emp_id, salary)
#         self.language = language
#     def write_code(self):
#         print(self.name, "is coding in", self.language)
# class Manager(Employee):
#     def conduct_meeting(self):
#         print(self.name, "is conducting a meeting")
# dev1 = Developer("bob", 12, 11111, "python")
# man1 = Manager("john", 13, 11112)
# dev1.display()
# man1.display()
# dev1.write_code()
# man1.conduct_meeting()

# 5. 
# Vehicle
#  /    \
# Car   Bike
# Both classes should inherit `start()` and have their own movement methods.

# class Vehicle:
#     def start(self):
#         print("vehicles are start")
# class Car(Vehicle):
#     def start(self):
#         print("car is starting")
# class Bike(Vehicle):
#     def start(self):
#         print("bike is starting")
# car = Car()
# bike = Bike()
# car.start()
# bike.start()

# 6. Create two parent classes:
# Father
# Mother
#    ↓
# Child
# Demonstrate multiple inheritance.

# class Father:
#     def driving(self):
#         print("father can drive")
# class Mother:
#     def cooking(self):
#         print("mother can cook")
# class Child(Father, Mother):
#     def playing(self):
#         print("children can play")
# child = Child()
# child.cooking()
# child.driving()
# child.playing()

# 7. Create an abstract Shape class with an abstract method:
# area()
# Create Circle as a child class.

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         print(3.14 * self.radius ** 2)
# a = Circle(5)
# a.area()

# 8. Create an abstract Animal class with an abstract sound() method. Create a Dog class that implements it.

# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("dog is barking")
# dog = Dog()
# dog.sound()

# 9. Create an abstract Vehicle class with an abstract start() method. Implement it in Car and Bike.

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("Car engine is starting")
# class Bike(Vehicle):
#     def start(self):
#         print("Bike engine is starting")
# car = Car()
# bike = Bike()
# car.start()
# bike.start()

# 10. Create an abstract Shape class with an abstract area() method. Implement it in Rectangle.

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# a = Rectangle(10, 10)
# print(a.area())




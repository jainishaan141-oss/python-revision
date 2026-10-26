# 1. Create a `Circle` class with radius.
# Create methods to calculate:
# - Area
# - Circumference

# class Circle:
#     def __init__(self, area = 0, circumference = 0, pi = 3.14, radius = 5):
#         self.area = area
#         self.circumference = circumference
#         self.pi = pi
#         self.radius = radius
#     def display(self):
#         print("area :", self.pi * self.radius ** 2)
#         print("circumference :", 2 * self.pi * self.radius)
# circle = Circle()
# circle.display()

# 2. Create an `Employee` class with:
# - Name
# - Salary
# Create a method that increases salary by 10%.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def increase_salary(self):
#         self.salary *= 1.10
# emp1 = Employee("bob", 10000)
# print(f"before increase {emp1.name}: {emp1.salary :}$")
# emp1.increase_salary()
# print(f"after increase {emp1.name}: {emp1.salary :}$")

# 3. Create a `Laptop` class with:
# - Brand
# - RAM
# - Storage
# Create a method to display all specifications.

# class Laptop:
#     def __init__(self, brand, ram, storage):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#     def display(self):
#         print("brand :", self.brand)
#         print("ram :", self.ram)
#         print("storage :", self.storage)
# lap1 = Laptop("Apple", "16GB", "512 SSD")
# lap1.display()

# 4. Create a `Rectangle` class with length and width.
# Create methods for:
# - Area
# - Perimeter

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def display(self):
#         print("area :", self.length * self.width)
#         print("perimeter :", 2 * self.length + self.width)
# s1 = Rectangle(5, 5)
# s1.display()

# 5. Student Marks
# Create a Student class with:
# Name
# Roll number
# Marks
# Create a method to display the data and another method to check pass/fail.

# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#     def display(self):
#         print("name :", self.name)
#         print("roll_no :", self.roll_no)
#         print("marks :", self.marks)
#     def check_marks(self):
#         if self.marks >= 40:
#             print("result : pass")
#         else:
#             print("result : fail")
# s1 = Student("ishaan", 12, 90)
# s1.display()
# s1.check_marks()

# 6. Create a `Rectangle` class with:
# - Length
# - Width
# Create methods to calculate:
# - Area
# - Perimeter

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def display(self):
#         print("area:", self.length * self.width)
#         print("perimeter:", 2 * (self.length + self.width))
# s1 = Rectangle(5, 5)
# s1.display()
# s2 = Rectangle(2, 2)
# s2.display()


# 7. Create a `Student` class with marks.
# Create a method that returns:
# A Grade → 90 and above
# B Grade → 75 to 89
# C Grade → 50 to 74
# Fail → Below 50

# class Student:
#     def __init__(self, marks):
#         self.marks = marks  
#     def calculate_grade(self):
#         if self.marks >= 90:
#             return "A Grade"
#         elif self.marks >= 75:
#             return "B Grade"
#         elif self.marks >= 50:
#             return "C Grade"
#         else:
#             return "Fail"
# student1 = Student(95)
# student2 = Student(82)
# student3 = Student(64)
# student4 = Student(45)
# print(f"Student 1 Marks: {student1.marks} -> {student1.calculate_grade()}")
# print(f"Student 2 Marks: {student2.marks} -> {student2.calculate_grade()}")
# print(f"Student 3 Marks: {student3.marks} -> {student3.calculate_grade()}")
# print(f"Student 4 Marks: {student4.marks} -> {student4.calculate_grade()}")


# 8. Create a `BankAccount` class.
# Implement:
# - Deposit
# - Withdraw
# - Check balance
# Do not allow withdrawal greater than the available balance.

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print(self.balance)
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(self.balance)
#         else:
#             print("insuficient balance")
# s1 = BankAccount("ishaan", 200000)
# s1
# s1.deposit(5000)
# s1.withdraw(3000)

# 9. Create an `Animal` parent class and `Dog` child class. Demonstrate inherited and child-specific methods.

# class Animal:
#     def eat(self):
#         print("animals is eating")
# class Dog(Animal):
#     def bark(self):
#         print("dog is barking")
# dog = Dog()
# dog.eat()
# dog.bark()

# 2. Create:
# Person → Student
# Person should contain name and age. Student should contain roll number.
# Use `super()`.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Student(Person):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no
# s1 = Student("bob", 18, "H-12")
# print("name :", s1.name)
# print("age :", s1.age)
# print("roll_no :", s1.roll_no)




# 22. Shallow copy vs deep copy 
# Demonstrate the difference using nested lists and explain how changes to nested objects behave.

# a = [[1, 2], [3, 4]]
# shallow = []
# deep = []
# for x in a:
#     shallow.append(x)          
#     y = []
#     for i in x:
#         y.append(i)            
#     deep.append(y)
# a[0][0] = 99
# print("original:", a)
# print("shallow :", shallow)    
# print("deep    :", deep)       

# 23. Create a BankAccount class 
# Implement deposit, withdrawal, and balance-checking methods. 

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#     def deposit(self, amt):
#         self.balance += amt
#     def withdraw(self, amt):
#         if amt > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amt
#     def check(self):
#         print("Balance:", self.balance)
# acc = BankAccount(1000)
# acc.deposit(500)
# acc.withdraw(300)
# acc.withdraw(5000)
# acc.check()

# 24. Demonstrate inheritance 
# Create a parent class Employee and child classes Manager and Developer. 

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def show(self):
#         print("Employee:", self.name, self.salary)
# class Manager(Employee):
#     def show(self):
#         print("Manager:", self.name, self.salary)
# class Developer(Employee):
#     def show(self):
#         print("Developer:", self.name, self.salary)
# Employee("Ravi", 30000).show()
# Manager("Amit", 90000).show()
# Developer("Neha", 70000).show()

# 25. Demonstrate encapsulation 
# Keep a bank account balance private and provide methods to access and update it safely. 

# class Account:
#     def __init__(self, balance):
#         self.__balance = balance          
#     def get_balance(self):
#         return self.__balance
#     def deposit(self, amt):
#         if amt > 0:
#             self.__balance += amt
#     def withdraw(self, amt):
#         if 0 < amt <= self.__balance:
#             self.__balance -= amt
# a = Account(1000)
# a.deposit(500)
# a.withdraw(200)
# print(a.get_balance())

# 26. Create a custom exception 
# Define InsufficientBalanceError and raise it when a withdrawal exceeds the available balance. 

# class InsufficientBalanceError(Exception):
#     pass
# class Account:
#     def __init__(self, balance):
#         self.balance = balance
#     def withdraw(self, amt):
#         if amt > self.balance:
#             raise InsufficientBalanceError("Not enough balance")
#         self.balance -= amt
# try:
#     Account(1000).withdraw(2000)
# except InsufficientBalanceError as e:
#     print("Error:", e)

# 27. Analyze a text file 
# Count lines, words, and characters in a text file. Handle the case where the file does not exist. 

# name = input("File name: ")
# try:
#     f = open(name)
#     lines = words = chars = 0
#     for line in f:
#         lines += 1
#         inword = False
#         for c in line:
#             chars += 1
#             if c in " \n\t":
#                 inword = False
#             elif not inword:
#                 inword = True
#                 words += 1
#     f.close()
#     print("Lines:", lines, "Words:", words, "Characters:", chars)
# except FileNotFoundError:
#     print("File does not exist")

# 28. Create a timing decorator 
# Write a decorator that measures and prints how long a function takes to execute. 


# 29. Create a generator 
# Use a generator to yield squares from 1 to N without building a complete list in memory. 

# def squares(n):
#     for i in range(1, n + 1):
#         yield i * i
# for x in squares(5):
#     print(x)

# 30. Build an employee management system 
# Use classes, file handling, and exception handling to add employees, display records, search by employee ID, and save/load records.





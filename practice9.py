# 1. Create an abstract Payment class with pay(amount). Implement it using UPI and CreditCard.

# from abc import ABC, abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount : float) -> None:
#         pass
# class UPI(Payment):
#     def pay(self, amount : float) -> None:
#         print(f"paid {amount} using UPI")
# class CreditCard(Payment):
#     def pay(self, amount : float) -> None:
#         print(f"paid {amount} using CreditCard")
# def process_payment(payment_method : Payment, amount : float) -> None:
#     payment_method.pay(amount)
# upi_payment = UPI()
# cc_payment = CreditCard()
# process_payment(upi_payment, 100.0)
# process_payment(cc_payment, 2500.5)

# 2. Create an abstract `Employee` class with `calculate_salary()`. Create:
# - `FullTimeEmployee`
# - `PartTimeEmployee`

# from abc import ABC, abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
# class FullTimeEmployee(Employee):
#     def __init__(self, monthly_salary):
#         self.monthly_salary = monthly_salary
#     def calculate_salary(self):
#         return self.monthly_salary 
# class PartTimeEmployee(Employee):
#     def __init__(self, hourly_rate, hours_worked):
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked
#     def calculate_salary(self):
#         return self.hourly_rate * self.hours_worked
# full_time = FullTimeEmployee(5000.0)
# part_time = PartTimeEmployee(20.0, 80.0)
# print(full_time.calculate_salary())
# print(part_time.calculate_salary())

# 3. Create a Student class with a public name and marks. Create an object and access both directly.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
# s1 = Student("bob", 80)
# print(s1.name, s1.marks)
        
# 4. Create an `Employee` class with a protected variable:
# _salary
# Create a child class and access the salary from the child.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
# class Manager(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#     def display_salary(self):
#         print(f"{self.name} salary is ${self.salary}")
# mgr = Manager("bob", 95000)
# mgr.display_salary()
        





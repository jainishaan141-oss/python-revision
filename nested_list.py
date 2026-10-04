# students = [
#     ["ishaan", 17],
#     ["bob", 16],
#     ["john", 15]
# ]
# print(students)

# students = [
#     ["ishaan", 17],
#     ["bob", 16],
#     ["john", 15]
# ]
# print(students[0][0])
# print(students[1][1])

# students = [
#     ["ishaan", 17],
#     ["bob", 16],
#     ["john", 15]
# ]
# students[1][1] = 19
# print(students)

# students = [
#     ["ishaan", 17],
#     ["bob", 16],
#     ["john", 15]
# ]
# for student in students:
#     print(student)

# students = [
#     ["ishaan", 17],
#     ["bob", 16],
#     ["john", 15]
# ]
# for student in students:
#     print("name:", student[0])
#     print("marks:", student[1])
# print()

# numbers = [i for i in range(1, 11)]
# print(numbers)

# squares= [i*i for i in range(1,6)]
# print(squares)

# even= [i for i in range(2,21,2)]
# print(even)

# even = [i for i in range(1, 21) if i %2 == 0]
# print(even)

# words= ["Python", "Java", "C", "JavaScript"]
# long_words= [word for word in words if len(word) > 4]
# print(long_words)

# students= [
#     ["Rahul",85],
#     ["Riya",35],
#     ["Aman",72]
# ]
# for student in students:
#     name = student[0]
#     marks = student[1]
#     print("Name:",name)
#     print("Marks:",marks)
#     if marks >= 40:
#         print("Result: Pass")
#     else:
#         print("Result: Fail")
# print()

# cart= [
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Keyboard", 1200]
# ]
# total = 0
# for item in cart:
#     product = item[0]
#     price = item[1]
#     print(product,"-",price)
#     total += price
#     print("Total Bill =",total)

# students= [
#     ["Rahul",20],
#     ["Riya",19],
#     ["Aman",21]
# ]
# for student in students:
#     print("Name:",student[0])
#     print("Age:",student[1])

# books= [
#     ["Python",450],
#     ["Java",500],
#     ["C++",400]
# ]
# for book in books:
#     print(book[0],"-",book[1])

# squares= [i*i for i in range(1,11)]
# print(squares)

# odd= [i for i in range(1,21) if i %2 !=0]
# print(odd)

# names= ["Rahul", "Alexander", "Riya" , "Jennifer"]
# result= [name for name in names if len(name) > 5]
# print(result)

# Create a nested list containing five students and their marks.

# students = [
#     ["ishaan", 18],
#     ["bob", 25],
#     ["john", 55],
#     ["alex", 11],
#     ["riya", 99]
# ]
# for i in students:
#     print(i[0])
#     print(i[1])

# Print only the names from a nested student list.

# students = [
#     ["ishaan", 18],
#     ["bob", 25],
#     ["john", 55],
#     ["alex", 11],
#     ["riya", 99]
# ]
# for i in students:
#     print(i[0])

# Update the marks of the second student in a nested list.

# students = [
#     ["ishaan", 75],
#     ["bob", 30],
#     ["john", 45]
# ]
# students[1][1] = 100
# print(students) 

# Create a list of numbers from 1 to 20 using list comprehension.

# num = [i for i in range(1 , 21)]
# print(num)

# Create a list of cubes from 1 to 10 using list comprehension.

# cube = [i * i * i for i in range(1 , 11)]
# print(cube)

# Create a list of all numbers divisible by 5 between 1 and 100 using list comprehension.

# num = [i for i in range(1 , 101) if i % 5== 0]
# print(num)

# Create a list containing only words that start with the letter "P" from a given list.

# a = ["ishaan", "punit", "putin"]
# char = 'p'
# result = [word for word in a if word.startswith(char)]
# print(result)

# Create a shopping cart with four products and display the total bill.

# products = [
#     ["laptop", 40000],
#     ["mouse", 2000],
#     ["keyboard", 4000]
# ]
# total_bill = 0
# price = products[1] 
# for i in products:
#     print(i[0])
#     print(i[1])
#     print(products,"-",price)
# total_bill += price
# print("total_bill  =",total_bill)

# Create a student marks system that displays the grade:
# A: 90 and above
# B: 75–89
# C: 50–74
# F: Below 50

# students = [
#     ("Alice", 92),
#     ("Bob", 84),
#     ("john", 65),
#     ("riya", 42),
# ]
# for name, marks in students:
#     if marks >= 90:
#         print("A grade")
#     elif marks >= 75:
#         print("B grade")
#     elif marks >= 50:
#         print("C grade")
#     else:
#         print("fail")
#     print(f"name: {name} | marks : {marks}")

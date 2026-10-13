# Part 1: Dictionary and Set — 30 Coding Questions
# Dictionary: Questions 1–15
# Access, update, counting, frequency maps and problem-solving

## Level 1 — Dictionary Fundamentals

# 1. Create and display a dictionary
# Create a dictionary containing a student's name, age, course and marks. Print each key and value using a for loop.

# students = {
#     "name" : "ishaan",
#     "age" : 17,
#     "course" : "IT",
#     "marks" : 90
# }
# for key, values in students.items():
#     print(key, ":", values)

# 2. Search for a key
# Given a student dictionary, check whether the key `"email"` exists. Print `"Found"` or `"Not found"` without causing a `KeyError`.

# students = {
#     "name" : "ishaan",
#     "age" : 17,
#     "course" : "IT",
#     "marks" : 90,
#     "email" : "jainishaan141@gmail.com"
# }
# if "email" in students:
#     print("found")
# else:
#     print("not found")

# 3. Count dictionary entries
# Find the number of key-value pairs in a dictionary without using len().

# students = {
#     "name" : "ishaan",
#     "age" : 17,
#     "course" : "IT",
#     "marks" : 90,
#     "email" : "jainishaan141@gmail.com"
# }
# count = 0
# for key in students:
#     count += 1
# print(count)

# 4. Update a student's marks
# Given {"Aman": 75, "Riya": 82, "Karan": 68}, update Riya's marks to 90 and display the updated dictionary.

# students = {
#     "Aman" : 75, 
#     "Riya" : 82, 
#     "Karan": 68
# }
# students["Riya"] = 90
# print(students)

# 5. Find the student with the highest marks
# Given a dictionary of student names and marks, find the student with the highest marks without using max().

# students = {
#     "Aman" : 75, 
#     "Riya" : 82, 
#     "Karan": 68
# }
# highest_name = ""
# highest_marks = 0
# for name in students:
#     if students[name] > highest_marks:
#         highest_marks = students[name]
#         highest_name = name
# print(highest_name, highest_marks)

# Level 2 — Counting and Transformation

# 6. Calculate the average marks
# Given a dictionary of student names and marks, calculate the average marks using a loop.

# students = {
#     "Aman" : 75, 
#     "Riya" : 82, 
#     "Karan": 68
# }
# total = 0
# count = 0 
# for name in students:
#     total += students[name]
#     count += 1
# average = total / count
# print(average)

# 7. Count passing and failing students
# Given a marks dictionary, count how many students scored at least 40 and how many scored below 40.

# marks = {
#     "bob" : 40,
#     "john" : 90,
#     "riya" : 85,
#     "aman" : 32
# }
# passed = 0
# failed = 0
# for num in marks.values():
#     if num >= 40:
#         passed += 1
#     else:
#         failed += 1
# print(passed)
# print(failed)

# 8. Create a dictionary from two lists
# Convert ["name", "age", "city"] and ["Aman", 20, "Bonn"] into a dictionary without using zip().

# keys = [
#     "name",
#     "age",
#     "city"
# ]
# values = [
#     "aman", 
#     20,
#     "Bonn"
# ]
# result = {}
# count = 0
# for key in keys:
#     result[key] = values[count]
#     count += 1
# print(result)

# 9. Invert a dictionary
# Convert {"A": 1, "B": 2, "C": 3} into {1: "A", 2: "B", 3: "C"}. Assume the original values are unique.

# dic = {
#     "A" : 1, 
#     "B" : 2, 
#     "C" : 3
# }
# reverse = {}
# for key in dic:
#     value = dic[key]
#     reverse[value] = key
# print(reverse)

# 10. Merge two dictionaries
# Merge two dictionaries. If a key exists in both, add the two values together.

# dic1 = {
#     "a" : 10, 
#     "b" : 20
# }
# dic2 = {
#     "b" : 5,
#     "c" : 30
# }
# add = {}
# for key in dic1:
#     add[key] = dic1[key]
# for key in dic2:
#     if key in add:
#         add[key] += dic2[key]
#     else:
#         add[key] = dic2[key]
# print(add)



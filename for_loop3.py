# Level 5 — String Logic Using `for`
# Now apply the same thinking to strings.

# 21. Count vowels in a string

# count = 0
# text = "Python Programming"
# for char in text:
#     if char in "aeiouAEIOU":
#         count = count + 1
# print(count)

# 22. Count consonants in a string

# count = 0
# text = "Python"
# for char in text:
#     if char not in "aeiouAEIOU":
#         count = count + 1
# print(count)

# 23. Count uppercase and lowercase characters

# upper_count = 0
# lower_count = 0
# text = "PyThOn"
# for char in text:
#     if 'a' <= char <= 'z':
#         lower_count = lower_count + 1
#     elif 'A' <= char <= 'Z':
#         upper_count = upper_count + 1
# print(upper_count)
# print(lower_count)

# 24. Count how many times a particular character occurs
# Don't use .count().

# count = 0
# text = "programming"
# find = "r"
# for char in text:
#     if char == find:
#         count = count + 1
# print(count)

# 25. Reverse a string using a for loop

# text = "hello"
# reverse = ""
# for char in text:
#     reverse = char + reverse
# print(reverse)

# Level 6 — Pattern Logic
# Patterns are very useful for developing loop thinking.

# 26. Print this pattern
# *
# **
# ***
# ****
# *****

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end = " ")
#     print()

# 27. Print this pattern
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()

# 28. Print this pattern
# *****
# ****
# ***
# **
# *

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end = " ")
#     print()

# Level 7 — Interview-Oriented Basic Problems
# These are still based primarily on `for` loops but require more thought.

# 29. Check whether a number is prime

# num = int(input("enter number:"))
# is_prime = True
# for i in range(2, num):
#     if num % i == 0:
#         is_prime = False
#         break
#     if is_prime:
#         print("prime number")
#     else:
#         print("not a prime number")

# 30. Print all prime numbers between 1 and 100
# This is the **final challenge**.
# It combines:
# - nested `for` loops
# - conditions
# - counters/flags
# - understanding divisibility
# - problem decomposition









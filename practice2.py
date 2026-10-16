# Intermediate: Questions 11–20

# 11. Remove duplicate characters 
# Remove repeated characters while preserving order. Example: "programming" → "progamin".

# text = "programming"
# result = ""
# for ch in text:
#     found = False
#     for i in result:
#         if i == ch:
#             found = True
#     if not found:
#         result += ch
# print(result)

# 12. Count words in a sentence 
# Count words in a sentence. Example: "Python is easy to learn" → 5.

# text = "python is easy to learn"
# count = 0
# is_word = False
# for ch in text:
#     if ch != " ":
#         if not is_word:
#             count += 1
#             is_word = True
#     else:
#         is_word = False
# print(count)

# 13. Find the second-largest number 
# Find the second-largest distinct number in a list without using sort(), sorted(), or max().

# numbers = [1, 2, 3, 4, 5, 6, 7]
# first = second = float("-inf")
# for num in numbers:
#     if num > first:
#         second = first
#         first = num
#     elif first > num > second:
#         second = num
# print(first)
# print(second)

# 14. Separate even and odd numbers 
# Separate the even and odd values in a list into two different lists.

# numbers = [1, 2, 3, 4, 5, 6]
# even = []
# odd = []
# for num in numbers:
#     if num % 2 == 0:
#         even += [num]
#     else:
#         odd += [num]
# print(even)
# print(odd)

# 15. Find common elements in two lists 
# Use basic loops to identify elements present in both lists.

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# comman = []
# for a in list1:
#     for b in list2:
#         if a == b:
#             comman += [a]
# print(comman)

# 16. Sort a list without built-in sorting 
# Sort a list of numbers in ascending order without using sort() or sorted().

# numbers = [100, 1, 99, 2, 0, 101]
# length = 0
# for i in numbers:
#     length += 1
# for i in range(length):
#     for j in range(i + 1, length):
#         if numbers[i] > numbers[j]:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
# print(numbers)

# 17. Check whether two strings are anagrams 
# Determine whether two strings contain the same letters. Example: "listen", "silent" → True.

# text1 = "listen"
# text2 = "silent"
# is_anagram = True
# for ch in text1 + text2:
#     count1 = 0
#     count2 = 0
#     for a in text1:
#         if a == ch:
#             count1 += 1
#     for b in text2:
#         if b == ch:
#             count2 += 1
#     if count1 != count2:
#         is_anagram = False
# print(is_anagram)

# 18. Student marks dictionary 
# Store students and their marks in a dictionary, then calculate each student's percentage and pass/fail status.

# students = {
#     "bob" : [80, 90, 100],
#     "riya" : [35, 40, 30],
#     "karan" : [60, 55, 75]
# }
# for name in students:
#     total = 0
#     count = 0
#     for i in students[name]:
#         total += i
#         count += 1
#         percentage = total / count
#         if percentage >= 40:
#             status = "pass"
#         else:
#             status = "fail"
#         print(name, "-", status)

# 19. Calculate simple interest 
# Write a function that calculates simple interest using principal, rate, and time.

# p = int(input("enter principle:"))
# r = int(input("enter rate:"))
# t = int(input("enter time:"))
# si = (p * r * t) / 100
# print(si)

# 20. Build a calculator 
# Use functions for addition, subtraction, multiplication, and division. Handle division by zero.

# num1 = float(input("enter first number:"))
# num2 = float(input("enter second number:"))
# operator = input("enter operator(+, -, *, /):")
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     if num2 == 0:
#         print("error: zero division error")
#     else:
#         print(num1 / num2)
# else:
#     print("invalid operator")




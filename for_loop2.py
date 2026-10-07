# Level 3 — Number Logic
# Now start making the student think about **what information must be maintained while looping**.

# 11. Print the multiplication table of a number

# num = int(input("enter number:"))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# 12. Find the factorial of a number

# num = int(input("enter number:"))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print(factorial)

# 13. Find the largest number from 5 user-entered numbers
# Important: Don't use max().

# largest = 0
# for i in range(5):
#     num = int(input("enter number:"))
#     if num > largest:
#         largest = num
# print(largest)

# 14. Find the smallest number from 5 user-entered numbers
# Don't use `min()`.

# smallest = 0
# for i in range(5):
#     num = int(input("enter number:"))
#     if num < smallest:
#         smallest = num
# print(smallest)

# 15. Find the average of 5 numbers entered by the user
# This teaches:
# sum → count → average

# sum = 0
# for i in range(5):
#     num = int(input("enter number:"))
#     sum = sum + num
# average = sum / 5
# print(average)

# Level 4 — Digit Logic
# This is where actual problem-solving starts.

# 16. Count the number of digits in a number
# **Constraint:** Use a `for` loop.
# A good approach is to treat the number as a string.

# num = 1234567
# count = 0
# for i in str(num):
#     count = count + 1
# print(count)

# 17. Find the sum of digits

# num = 12345
# sum = 0
# for i in str(num):
#     sum = sum + int(i)
# print(sum)

# 18. Find the product of digits

# num = 1234
# product = 1
# for i in str(num):
#     product = product * int(i)
# print(product)

# 19. Count how many even digits are present

# num = 12345678
# even_digit = 0
# for i in str(num):
#     if int(i) %2 == 0:
#         even_digit = even_digit + 1
# print(even_digit)

# 20. Find the largest digit in a number

# num = 58321
# largest = 0
# for i in num:
    



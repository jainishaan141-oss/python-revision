# Beginner: Questions 1–10

# 1. Reverse a string
# reverse a string Reverse a string without using slicing. Example: "Python" → "nohtyP".

# text = "Python"
# reverse = ""
# for char in text:
#     reverse = char + reverse
# print(reverse)

# 2. Check for a palindrome
# Check whether a string reads the same forward and backward. Example: "madam" → True.

# text = "racecar"
# n = 0
# for ch in text:
#     n += 1
# is_palindrome = True
# for i in range(n // 2):
#     if text[i] != text[n - 1 - i]:
#         is_palindrome = False
# print(is_palindrome)

# 3. Count vowels and consonants 
# Count vowels and consonants in a string. Example: "Python" → Vowels: 1, Consonants: 5.

# text = "aeroplane"
# vowels = 0
# consonants = 0
# for ch in text:
#     if ch in "aeiouAEIOU":
#         vowels += 1
#     elif(ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
#         consonants += 1
# print(vowels)
# print(consonants)

# 4. Find a factorial 
# Calculate the factorial of a number using a loop. Example: 5 → 120.

# number = int(input("enter number:"))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print(factorial)

# 5. Check for a prime number 
# Determine whether an integer is prime. Example: 17 → True.

# number = int(input("enter number:"))
# count = 0
# for i in range(1, number + 1):
#     if number % i == 0:
#         count += 1
# if(count == 2):
#     print(True)
# else:
#     print(False)

# 6. Print the Fibonacci series 
# Print the first N Fibonacci terms. Example: N = 7 → 0 1 1 2 3 5 8.

# num = int(input("enter number:"))
# a = 0
# b = 1
# for i in range(num):
#     print(a, end = " ")
#     c = a + b
#     a = b
#     b = c

# 7. Check for an Armstrong number 
# Check whether a number equals the sum of its digits raised to the number of digits. Example: 153 → True.

# 8. Count character frequency 
# Count how often each character appears. Example: "hello" → h:1, e:1, l:2, o:1.

# text = "python"
# frequency = {}
# for ch in text:
#     if ch in frequency:
#         frequency[ch] += 1
#     else:
#         frequency[ch] = 1
# print(frequency)

# 9. Sum the digits of a number 
# Calculate the digit sum without converting the number to a string. Example: 1234 → 10.

# num = 12345
# total = 0
# while num > 0:
#     total += num % 10
#     num //= 10
# print(total)

# 10. Print a number pattern 
# Use nested loops to print the following pattern: 
# 1 
# 12 
# 123 
# 1234 
# 12345

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()



# Class 8 (List and Tuple)
## Level 1 — List and Tuple Fundamentals (Questions 1–10)
# Focus: indexing, traversal, updating, adding and removing elements.

# 1. Create a list of 5 numbers and print each element using a for loop.

# numbers = [10, 20, 30, 40, 50]
# for num in numbers:
#     print(num)

# 2. Print the first and last elements of a list without hardcoding their values.

# num = [10, 20, 30, 40]
# first = num[0]
# last = num[-1]
# print(first, last)

# 3. Find the length of a list without using len().

# num = [10, 20, 30, 40]
# count = 0
# for item in num:
#     count = count + 1
# print(count)

# 4. Calculate the sum of all list elements without using sum().

# numbers = [10, 20, 30, 40]
# sum = 0
# for num in numbers:
#     sum = sum + num
# print(sum)

# 5. Find the average of numbers in a list.

# numbers = [10, 20, 30, 40]
# sum = 0
# count = 0
# for num in numbers:
#     sum = sum + num
#     count = count + 1
# average = sum / count 
# print(average)

# 6. Count the even and odd numbers in a list.

# numbers = [1, 2, 3, 4, 5, 6]
# even_count = 0
# odd_count = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_count = even_count + 1
#     else:
#         odd_count = odd_count + 1
# print(even_count)
# print(odd_count)

# 7. Find the largest element without using max().

# numbers = [1, 10, 0, 11]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(largest)

# 8. Find the smallest element without using min().

# numbers = [1, 10, 0, 11]
# smallest = numbers[0]
# for num in numbers:
#     if num < smallest:
#         smallest = num
# print(smallest)

# 9. Create a new list containing the squares of all elements.

# numbers = [2, 5, 7, 9, 11]
# for num in numbers:
#     print(num ** 2)

# 10. Convert a list into a tuple and a tuple into a list.

# list = [1, 2, 3]
# tuple = (*list,)
# print(tuple)

# tuple = (1, 2, 3)
# list = [*tuple,]
# print(list)



